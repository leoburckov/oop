import pytest

from src.category import Category
from src.product import Product


def test_category_init_and_products():
    p1 = Product("Test1", "Desc", 100.0, 5)
    p2 = Product("Test2", "Desc", 200.0, 10)
    category = Category("TestCat", "Category for tests", [p1, p2])

    assert category.name == "TestCat"
    assert "Test1" in category.products
    assert "Test2" in category.products


def test_add_product_valid():
    p = Product("Test", "Desc", 100.0, 5)
    category = Category("TestCat", "Category for tests")
    category.add_product(p)

    assert "Test" in category.products


def test_add_product_invalid():
    category = Category("TestCat", "Category for tests")
    with pytest.raises(TypeError):
        category.add_product("not a product")


def test_average_price():
    p1 = Product("Test1", "Desc", 100.0, 5)
    p2 = Product("Test2", "Desc", 200.0, 10)
    category = Category("TestCat", "Category for tests", [p1, p2])

    assert category.average_price() == 150.0


def test_average_price_empty():
    category = Category("Empty", "No products", [])
    assert category.average_price() == 0.0
