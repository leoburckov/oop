import pytest

from src.category import Category
from src.product import Product


def test_add_product():
    category = Category("Ноутбуки", "Игровые ноутбуки")
    product = Product("ASUS TUF", "RTX 4060, i7", 120000, 5)

    category.add_product(product)

    # Проверка количества продуктов через геттер
    assert "ASUS TUF, 120000 руб. Остаток: 5 шт." in category.products


def test_products_property_output():
    category = Category("Телевизоры", "Большие экраны")
    product1 = Product('Samsung 55"', "Smart TV", 70000, 2)
    product2 = Product('LG 65"', "OLED", 110000, 1)

    category.add_product(product1)
    category.add_product(product2)

    output = category.products
    assert 'Samsung 55", 70000 руб. Остаток: 2 шт.' in output
    assert 'LG 65", 110000 руб. Остаток: 1 шт.' in output


def test_private_product_list_access():
    category = Category("Смартфоны", "Флагманы")
    # Проверка, что _products (приватный атрибут) не является публичным
    with pytest.raises(AttributeError):
        _ = category.products_list  # должен отсутствовать

    # Но при этом products должен работать
    assert isinstance(category.products, str)
