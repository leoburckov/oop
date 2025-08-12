import pytest

from src.product import LawnGrass, Product, Smartphone


def test_product_init():
    p = Product("Test", "Description", 100.0, 5)
    assert p.name == "Test"
    assert p.price == 100.0
    assert p.quantity == 5


def test_price_setter_valid():
    p = Product("Test", "Description", 100.0, 5)
    p.price = 200.0
    assert p.price == 200.0


def test_price_setter_invalid(capsys):
    p = Product("Test", "Description", 100.0, 5)
    p.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть" in captured.out
    assert p.price == 100.0


def test_add_same_type():
    p1 = Product("Test", "Description", 100.0, 5)
    p2 = Product("Test", "Description", 100.0, 3)
    assert p1 + p2 == 8


def test_add_different_type():
    p1 = Product("Test", "Description", 100.0, 5)
    p2 = Smartphone("Phone", "Desc", 1000, 2, 95.5, "Model", 128, "Black")
    with pytest.raises(TypeError):
        _ = p1 + p2


def test_new_product():
    data = {"name": "Test", "description": "Desc", "price": 100.0, "quantity": 5}
    p = Product.new_product(data)
    assert isinstance(p, Product)
    assert p.name == "Test"


def test_smartphone_init():
    s = Smartphone("Phone", "Desc", 1000, 2, 95.5, "Model", 128, "Black")
    assert s.memory == 128
    assert s.color == "Black"


def test_lawngrass_init():
    g = LawnGrass("Grass", "Desc", 500, 10, "Россия", "7 дней", "Зеленый")
    assert g.country == "Россия"
    assert g.color == "Зеленый"
