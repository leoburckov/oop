import pytest

from src.category import Category
from src.product import Product, Smartphone


def test_category_initialization():
    p1 = Product("P1", "Desc", 100.0, 1)
    cat = Category("Test Cat", "Test Desc", [p1])
    assert cat.name == "Test Cat"
    assert len(cat.products) == 1


def test_add_product_valid():
    cat = Category("Phones", "Phone Category")
    phone = Smartphone("Phone", "Desc", 200.0, 5, 95.5, "X1", 128, "Black")
    cat.add_product(phone)
    assert len(cat.products) == 1


def test_add_product_invalid():
    cat = Category("Phones", "Phone Category")
    with pytest.raises(TypeError):
        cat.add_product("not a product")


def test_products_getter():
    phone = Smartphone("Phone", "Desc", 200.0, 5, 95.5, "X1", 128, "Black")
    cat = Category("Phones", "Phone Category", [phone])
    result = cat.products
    assert isinstance(result, list)
    assert "Phone" in result[0]
