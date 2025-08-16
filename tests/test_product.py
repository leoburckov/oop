import pytest

from src.product import LawnGrass, Product, Smartphone


def test_product_init_valid():
    product = Product("Test", "Description", 100.0, 10)
    assert product.name == "Test"
    assert product.description == "Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_product_init_zero_quantity():
    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        Product("Test", "Description", 100.0, 0)


def test_price_setter_valid():
    product = Product("Test", "Description", 100.0, 10)
    product.price = 200.0
    assert product.price == 200.0


def test_price_setter_invalid(capfd):
    product = Product("Test", "Description", 100.0, 10)
    product.price = -50
    out, _ = capfd.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in out
    assert product.price == 100.0


def test_add_products_same_type():
    p1 = Product("Test1", "Desc", 100.0, 5)
    p2 = Product("Test2", "Desc", 200.0, 7)
    assert p1 + p2 == 12


def test_add_products_different_type():
    p1 = Product("Test1", "Desc", 100.0, 5)
    s1 = Smartphone("Phone", "Smart", 1000.0, 3, 95.5, "X", 128, "Black")
    with pytest.raises(TypeError):
        _ = p1 + s1


def test_smartphone_init():
    phone = Smartphone("iPhone", "15 Pro", 150000.0, 5, 98.5, "15 Pro", 512, "Black")
    assert phone.model == "15 Pro"
    assert phone.memory == 512
    assert phone.color == "Black"


def test_lawngrass_init():
    grass = LawnGrass("Grass", "For lawn", 500.0, 20, "Russia", "7 days", "Green")
    assert grass.country == "Russia"
    assert grass.germination_period == "7 days"
    assert grass.color == "Green"
