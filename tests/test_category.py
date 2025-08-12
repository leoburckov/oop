import pytest

from src.category import Category
from src.product import LawnGrass, Smartphone


@pytest.fixture
def smartphones():
    return [
        Smartphone(
            "Samsung Galaxy S23 Ultra",
            "256GB, Серый цвет, 200MP камера",
            180000.0,
            5,
            95.5,
            "S23 Ultra",
            256,
            "Серый",
        ),
        Smartphone(
            "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
        ),
    ]


@pytest.fixture
def grasses():
    return [
        LawnGrass(
            "Газонная трава",
            "Элитная трава для газона",
            500.0,
            20,
            "Россия",
            "7 дней",
            "Зеленый",
        ),
        LawnGrass(
            "Газонная трава 2",
            "Выносливая трава",
            450.0,
            15,
            "США",
            "5 дней",
            "Темно-зеленый",
        ),
    ]


def test_category_initialization(smartphones):
    category = Category("Смартфоны", "Категория смартфонов", smartphones)
    assert category.name == "Смартфоны"
    assert category.description == "Категория смартфонов"
    assert len(category.products) == 2


def test_add_product_valid(smartphones):
    category = Category("Смартфоны", "Категория смартфонов", [])
    category.add_product(smartphones[0])
    assert len(category.products) == 1


def test_add_product_invalid():
    category = Category("Некорректная", "Пустая", [])
    with pytest.raises(TypeError):
        category.add_product("not a product")


def test_product_and_category_counts(smartphones, grasses):
    # При добавлении всех товаров через категории счетчики должны увеличиваться
    total_products = len(smartphones) + len(grasses)
    _ = Category("Phones", "desc", smartphones)
    _ = Category("Grass", "desc", grasses)
    assert Category.product_count >= total_products
    assert Category.category_count >= 2
