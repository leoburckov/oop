import pytest

from src.product import Product


def test_product_str():
    p = Product("TestPhone", "Описание", 100.0, 5)
    assert str(p) == "TestPhone, 100.0 руб. Остаток: 5 шт."


def test_product_price_getter_setter():
    p = Product("Test", "desc", 200.0, 1)
    assert p.price == 200.0
    p.price = 250.0
    assert p.price == 250.0


def test_product_price_setter_invalid():
    p = Product("Test", "desc", 100.0, 1)
    with pytest.raises(ValueError):
        p.price = -50


def test_product_addition():
    p1 = Product("A", "desc", 100.0, 2)
    p2 = Product("B", "desc", 200.0, 3)
    total = p1 + p2
    assert total == (100.0 * 2 + 200.0 * 3)
