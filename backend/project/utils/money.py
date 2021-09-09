from abc import ABC
from decimal import Decimal, ROUND_HALF_UP


class Money(ABC):
    """
    Абстрактный класс для работы с валютой
    """
    currency: Decimal   # минимальная "физическая" величина валюты (0.01 рубля, к примеру)


class RubMoney(Money):
    """
    Класс для комфортной работы с суммами в рублях
    """
    currency = Decimal('.01')

    @classmethod
    def get_min_value(cls) -> Decimal:
        """Получить минимальную валютную величину"""
        return cls.currency

    @classmethod
    def validate(cls, value: Decimal) -> None:
        """
        Проверка денежного значения

        :param value: денежное значение
        :return: None
        :raises ValueError: если значение `value` меньше, чем минимальная валютная величина `cls.currency`
        """
        if value < cls.currency:
            raise ValueError(f"value cant be lower then {cls.currency}")

    @classmethod
    def round(cls, value: Decimal) -> Decimal:
        """
        Округление денежного значения в соответствии с правилами денежного округления

        :param value: денежное значение
        :return: округленное денежное значение
        """
        cls.validate(value)
        return value.quantize(cls.currency, ROUND_HALF_UP)
