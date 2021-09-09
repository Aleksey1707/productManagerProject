from abc import ABC
from decimal import Decimal, ROUND_HALF_UP


class Money(ABC):
    currency: Decimal


class RubMoney(Money):
    currency = Decimal('.01')

    @classmethod
    def get_min_value(cls):
        return cls.currency

    @classmethod
    def validate(cls, value: Decimal):
        if value < cls.currency:
            raise ValueError(f"value cant be lower then {cls.currency}")

    @classmethod
    def round(cls, value: Decimal):
        cls.validate(value)
        return value.quantize(cls.currency, ROUND_HALF_UP)
