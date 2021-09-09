import decimal

import mptt.querysets
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from utils.money import RubMoney


class TimedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class CategoryQuerySet(mptt.querysets.TreeQuerySet):
    def head(self):
        """Головные категории"""
        return self.filter(parent_category__isnull=True)


class CategoryManager(mptt.models.TreeManager):
    def get_queryset(self):
        return CategoryQuerySet(self.model, using=self._db)

    def head(self):
        """Головные категории"""
        return self.get_queryset().head()


class Category(TimedModel, MPTTModel):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["created"]

    class MPTTMeta:
        order_insertion_by = ["name"]
        parent_attr = "parent_category"

    objects = CategoryManager()

    name = models.CharField(verbose_name="Наименование", max_length=255, unique=True,
                            validators=[MinLengthValidator(1, "Наименование категории не может быть пустым")])

    parent_category = TreeForeignKey("self", verbose_name="Родительская категория", on_delete=models.CASCADE,
                                     related_name='child_categories', null=True)

    def __str__(self):
        return self.name


class Product(TimedModel):
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        default_related_name = "products"

    name = models.CharField(verbose_name="Наименование", max_length=255,
                            validators=[MinLengthValidator(1, "Наименование продукта не может быть пустым")])
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

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
                                validators=[MinValueValidator(RubMoney.get_min_value(), "Цена не может быть меньше 0.01 рубля")])

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return f"Кол-во: {self.quantity}, цена {self.price}"
