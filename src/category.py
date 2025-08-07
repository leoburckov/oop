from typing import List, Union

from src.product import Product


class Category:
    category_count: int = 0
    product_count: int = 0

    def __init__(
        self, name: str, description: str, products: Union[List[Product], None] = None
    ):
        self.name = name
        self.description = description
        self.__products: List[Product] = []
        if products:
            for product in products:
                self.add_product(product)

        Category.category_count += 1

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты типа Product или его наследников"
            )
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        return "\n".join(
            [
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
                for product in self.__products
            ]
        )

    @classmethod
    def reset_counts(cls):
        cls.category_count = 0
        cls.product_count = 0
