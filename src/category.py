from typing import List

from src.product import Product


class Category:
    """Класс для категорий товаров."""

    category_count: int = 0
    product_count: int = 0

    def __init__(
        self, name: str, description: str, products: List[Product] | None = None
    ) -> None:
        self.name = name
        self.description = description
        self.__products: List[Product] = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    @property
    def products(self) -> List[str]:
        return [str(product) for product in self.__products]

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты класса Product или его наследников"
            )
        self.__products.append(product)
        Category.product_count += 1

    def middle_price(self) -> float:
        """Возвращает среднюю цену всех товаров в категории."""
        try:
            total_price = sum([p.price for p in self.__products])
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0.0
