from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов"""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def __add__(self, other: Any) -> float:
        """Складывает количество продуктов"""
        pass


class InfoMixin:
    """Миксин для вывода информации при создании объекта"""

    def __init__(self, *args, **kwargs) -> None:
        print(f"Создан объект {self.__class__.__name__} с параметрами: {args} {kwargs}")
        super().__init__(*args, **kwargs)


class Product(InfoMixin, BaseProduct):
    """Основной класс продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        super().__init__(name, description, price, quantity)
        self.__price = price
        Product.product_count += 1

    product_count = 0

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = value

    @classmethod
    def new_product(
        cls,
        name: str,
        description: str,
        price: float,
        quantity: int
    ) -> Product:
        return cls(name, description, price, quantity)

    def __add__(self, other: Any) -> float:
        if type(self) is not type(other):
            raise TypeError("Складывать можно только одинаковые типы продуктов")
        return self.quantity + other.quantity


class Smartphone(Product):
    """Класс для смартфонов"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для газонной травы"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
