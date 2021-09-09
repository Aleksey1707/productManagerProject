from django.test import TestCase

from django.core.exceptions import ValidationError

from product.models import Category, Product, Shop, ProductState
from utils.money import RubMoney


class TestCategory(TestCase):

    def test_name(self):
        category = Category()
        self.assertRaises(ValidationError, category.full_clean)

        name = "category 1"
        category.name = name
        self.assertEqual(category.name, name)


class TestProduct(TestCase):

    def test_name(self):
        product = Product()
        self.assertRaises(ValidationError, product.full_clean)

        name = "product 1"
        product.name = name
        self.assertEqual(product.name, name)


class TestShop(TestCase):

    def test_name(self):
        shop = Shop()
        self.assertRaises(ValidationError, shop.full_clean)

        name = "shop 1"
        shop.name = name
        self.assertEqual(shop.name, name)


class TestProductState(TestCase):

    def setUp(self) -> None:
        category = Category.objects.create(name="category 1")
        product = Product.objects.create(name="product 1", category=category)
        shop = Shop.objects.create(name="shop 1")
        self.product_state = ProductState(shop=shop, product=product)

    def test_quantity(self):
        self.product_state.price = RubMoney.get_min_value()
        self.assertRaises(ValidationError, self.product_state.full_clean)

        self.product_state.quantity = -15
        self.assertRaises(ValidationError, self.product_state.full_clean)

        self.product_state.quantity = 0
        self.product_state.full_clean()
