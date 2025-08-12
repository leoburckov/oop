import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def sample_products():
    return [Product("Test1", "Desc", 100.0, 5), Product("Test2", "Desc", 200.0, 3)]


def test_category_init(sample_products):
    c = Category("TestCat", "Description", sample_products)
    assert c.name == "TestCat"
    assert len(c.products) == 2


def test_add_product(sample_products):
    c = Category("TestCat", "Description", [])
    c.add_product(sample_products[0])
    assert len(c.products) == 1


def test_add_invalid_product():
    c = Category("TestCat", "Description", [])
    with pytest.raises(TypeError):
        c.add_product("Not a product")


def test_products_repr(sample_products):
    c = Category("TestCat", "Description", sample_products)
    for item in c.products:
        assert isinstance(item, str)
        assert "руб." in item
