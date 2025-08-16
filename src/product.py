from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, Any, cast


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self._price = value


class InfoMixin:
    """Миксин для вывода информации о создании объекта."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        class_name = self.__class__.__name__
        print(f"{class_name} создан с параметрами: {args}, {kwargs}")
        super().__init__(*args, **kwargs)


class Product(InfoMixin, BaseProduct):
    """Базовый класс для всех товаров."""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__(name, description, price, quantity)

    @classmethod
    def new_product(cls, data: Dict[str, Any]) -> Product:
        """Создает продукт из словаря с безопасным приведением типов."""
        return cls(
            cast(str, data.get("name")),
            cast(str, data.get("description")),
            float(cast(Any, data.get("price"))),
            int(cast(Any, data.get("quantity"))),
        )

    def __add__(self, other: object) -> int:
        if type(self) is not type(other):
            raise TypeError("Можно складывать только продукты одного класса")
        return self.quantity + other.quantity  # type: ignore

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


class Smartphone(Product):
    """Класс для смартфонов."""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для газонной травы."""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
