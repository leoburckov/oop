import pytest

from src.category import Category
from src.product import Product


def test_category_str():
    p1 = Product("A", "desc", 100, 5)
    p2 = Product("B", "desc", 200, 3)
    c = Category("Смартфоны", "Описание", [p1, p2])
    assert str(c) == "Смартфоны, количество продуктов: 8 шт."


def test_category_add_product_valid():
    c = Category("Техника", "Описание")
    p = Product("Монитор", "desc", 15000, 4)
    c.add_product(p)
    assert str(p) in c.products


def test_category_add_product_invalid():
    c = Category("Гаджеты", "Описание")
    with pytest.raises(TypeError):
        c.add_product("not a product")


def test_category_products_str():
    p1 = Product("A", "desc", 100, 1)
    p2 = Product("B", "desc", 200, 1)
    c = Category("Phones", "desc", [p1, p2])
    lines = c.products.split("\n")
    assert lines == [str(p1), str(p2)]
