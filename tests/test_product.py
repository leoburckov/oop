from src.product import Product


def test_product_init() -> None:
    p = Product("Телефон", "Смартфон", 19990.0, 10)
    assert p.name == "Телефон"
    assert p.price == 19990.0
    assert p.quantity == 10
