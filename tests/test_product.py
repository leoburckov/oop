from src.product import Product


def test_product_initial_price():
    product = Product("Test", "Test product", 100.0, 10)
    assert product.price == 100.0


def test_product_price_setter_valid():
    product = Product("Test", "Test product", 100.0, 10)
    product.price = 250.0
    assert product.price == 250.0


def test_product_price_setter_invalid(capfd):
    product = Product("Test", "Test product", 100.0, 10)
    product.price = -50.0  # недопустимое значение

    # Проверка, что цена не изменилась
    assert product.price == 100.0

    # Проверка, что в консоль выведено сообщение
    captured = capfd.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
