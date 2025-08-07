# Магазин товаров (Python)

Проект представляет собой систему управления товарами для магазина с использованием ООП.

## Функциональность

### 1. Классы-наследники
Реализованы два класса-наследника `Product`:
- **`Smartphone`** (Смартфон):
  - `efficiency` (производительность)
  - `model` (модель)
  - `memory` (объем памяти)
  - `color` (цвет)
  
- **`LawnGrass`** (Трава газонная):
  - `country` (страна-производитель)
  - `germination_period` (срок прорастания)
  - `color` (цвет)

### 2. Ограничения сложения
- Реализована проверка типов при сложении товаров:
  ```python
  smartphone1 + smartphone2  # OK
  lawn_grass + smartphone    # TypeError!
Используется type() для проверки совместимости типов

3. Ограничения добавления продукта
Защита от добавления некорректных объектов в категории:

python
category.add_product(smartphone)  # OK
category.add_product("not a product")  # ValueError!
Проверка через isinstance() и issubclass()

4. Тестирование
Написаны тесты для новой функциональности

Покрытие кода тестами >75%

Отчет о покрытии в coverage.xml/htmlcov/

Установка и запуск
Клонировать репозиторий:

bash
git clone https://github.com/yourusername/shop-project.git
cd shop-project
Установить зависимости:

bash
pip install -r requirements.txt
Запустить тесты:

bash
pytest --cov=.
Пример использования
python
from products import Product, Smartphone, LawnGrass
from category import Category

# Создание продуктов
iphone = Smartphone("iPhone 15", "Flagship smartphone", 999.99, 10,
                   efficiency="A16 Bionic", model="15 Pro",
                   memory=256, color="Space Gray")

grass = LawnGrass("Premium Grass", "Green lawn", 49.99, 100,
                 country="Netherlands",
                 germination_period=14, color="Emerald")

# Работа с категорией
electronics = Category("Electronics", "Tech products")
electronics.add_product(iphone)  # Успешно
electronics.add_product(grass)   # ValueError!
Структура проекта
text
shop/
├── __init__.py
├── products.py       # Базовый класс и наследники
├── category.py      # Логика работы с категориями
├── tests/
│   ├── test_products.py
│   └── test_category.py
├── main.py          # Пример использования
└── requirements.txt
Требования
Python 3.8+

pytest (для тестирования)

coverage (для отчетов)