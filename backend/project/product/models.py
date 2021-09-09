import decimal

from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from utils.model import CreatedModifiedMixin


class Category(models.Model, CreatedModifiedMixin):

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    name = models.CharField(verbose_name="Наименование", max_length=255,
                            validators=[MinLengthValidator(1, "Наименование категории не может быть пустым")])

    def __str__(self):
        return self.name


class Product(models.Model, CreatedModifiedMixin):

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

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


class Shop(models.Model, CreatedModifiedMixin):

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

    name = models.CharField(verbose_name="Наименование", max_length=255,
                            validators=[MinLengthValidator(1, "Наименование магазина не может быть пустым")])

    def __str__(self):
        return self.name


class ProductState(models.Model, CreatedModifiedMixin):

    class Meta:
        verbose_name = "Статус товара"
        verbose_name_plural = "Статус товаров"

    min_rub_value = decimal.Decimal(0.01).quantize(decimal.Decimal('.01'), decimal.ROUND_HALF_UP)

    quantity = models.IntegerField(verbose_name="Количество",
                                   validators=[MinValueValidator(0, "Количество товара не может быть ниже нуля")])

    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2,
                                validators=[MinValueValidator(min_rub_value, "Цена не может быть меньше 0.01 рубля")])

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return f"Кол-во: {self.quantity}, цена {self.price}"
