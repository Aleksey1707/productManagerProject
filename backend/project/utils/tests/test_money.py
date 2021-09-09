from decimal import Decimal
from unittest import TestCase

from utils.money import RubMoney


class TestRubMoney(TestCase):
    def test_min_value(self):
        self.assertEqual(str(RubMoney.get_min_value()), "0.01", "Минимальное денег в рублях должно быть равно 0.01")

    def test_validate(self):
        with self.assertRaises(ValueError):
            RubMoney.validate(Decimal('.0'))

    def test_round(self):
        summa = Decimal(0.5) + Decimal(65.9995)
        self.assertEqual(str(RubMoney.round(summa)), "66.50", "Минимальное денег в рублях должно быть равно 0.01")
