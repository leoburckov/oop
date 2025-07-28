from src.category import Category
from src.product import Product


def test_category_counts() -> None:
    Category.category_count = 0
    Category.product_count = 0

    products = [
        Product("Телефон", "Смартфон", 19990.0, 10),
        Product("Наушники", "Bluetooth", 3990.0, 5),
    ]
    c = Category("Электроника", "Техника", products)

    assert Category.category_count == 1
    assert Category.product_count == 2
    assert c.name == "Электроника"
