from __future__ import annotations
from typing import Optional
from src.product import Product


class Category:
    """Класс категории товаров"""

    category_count = 0
    product_count = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: Optional[list[Product]] = None
    ) -> None:
        self.name = name
        self.description = description
        self.__products: list[Product] = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    @property
    def products(self) -> str:
        """Возвращает список товаров в виде строки"""
        return "\n".join(
            f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт."
            for p in self.__products
        )

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию с проверкой типа"""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product или его наследников")
        self.__products.append(product)
        Category.product_count += 1
