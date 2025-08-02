from typing import List, Optional

from src.product import Product


class Category:
    category_count = 0
    product_count = 0

    def __init__(
        self, name: str, description: str, products: Optional[List[Product]] = None
    ):
        self.name = name
        self.description = description
        self.__products: List[Product] = products if products is not None else []

        Category.category_count += 1
        Category.product_count += sum(product.quantity for product in self.__products)

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты класса Product или его подклассов"
            )
        self.__products.append(product)
        Category.product_count += product.quantity

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self) -> str:
        return "\n".join(str(p) for p in self.__products)
