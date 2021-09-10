from django.conf import settings
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.db.models import Q
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from utils.money import RubMoney


class TimedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class Category(TimedModel, MPTTModel):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    name = models.CharField(verbose_name="Наименование", max_length=255, unique=True,
                            validators=[MinLengthValidator(1, "Наименование категории не может быть пустым")])

    parent = TreeForeignKey("self", verbose_name="Родительская категория", on_delete=models.CASCADE,
                            related_name='children', null=True, blank=True, db_index=True,
                            limit_choices_to=Q(level__lte=settings.MAX_CATEGORY_LEVEL - 1),
                            help_text=f"Максимальный допустимый уровень вложенности категории - "
                                      f"{settings.MAX_CATEGORY_LEVEL + 1}")

    def __str__(self):
        return self.name


class Product(TimedModel):
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        default_related_name = "products"

    name = models.CharField(verbose_name="Наименование", max_length=255,
                            validators=[MinLengthValidator(1, "Наименование продукта не может быть пустым")])
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 limit_choices_to=Q(children__isnull=True),
                                 help_text="Продукты можно добавлять только в категории, "
                                           "которые не имеют под категорий")

    shops = models.ManyToManyField(
        'Shop',
        through='ProductState',
        through_fields=('product', 'shop'),
        related_name='products'
    )

    def __str__(self):
        return self.name


class Shop(TimedModel):
    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"
        default_related_name = "shops"

    name = models.CharField(verbose_name="Наименование", max_length=255,
                            validators=[MinLengthValidator(1, "Наименование магазина не может быть пустым")])

    def __str__(self):
        return self.name


class ProductState(TimedModel):
    class Meta:
        verbose_name = "Статус товара"
        verbose_name_plural = "Статус товаров"
        default_related_name = "product_states"

    quantity = models.IntegerField(verbose_name="Количество",
                                   validators=[MinValueValidator(0, "Количество товара не может быть ниже нуля")])

    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2,
                                validators=[MinValueValidator(RubMoney.get_min_value(),
                                                              "Цена не может быть меньше 0.01 рубля")])

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name="Магазин")

    def __str__(self):
        return f"Кол-во: {self.quantity}, цена {self.price}"
