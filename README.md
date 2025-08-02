Вот пример README.md файла для вашего проекта, соответствующий текущей структуре и реализованной логике:

📱 Магазин электроники
Этот проект представляет собой простой консольный Python-приложение для моделирования продуктовой категории и товаров. Система позволяет создавать товары и категории, отслеживать количество созданных экземпляров и получать базовую информацию.

📂 Структура проекта
bash
Копировать
Редактировать
.
├── src
│   ├── __init__.py
│   ├── category.py        # Класс Category
│   ├── product.py         # Класс Product
├── tests
│   ├── __init__.py
│   ├── test_category.py   # Тесты для Category
│   ├── test_product.py    # Тесты для Product
├── main.py                # Точка входа
├── README.md              # Описание проекта
├── .gitignore
├── pyproject.toml         # Poetry-конфигурация
📦 Установка
bash
Копировать
Редактировать
git clone https://github.com/yourusername/oop-shop.git
cd oop-shop
poetry install
▶️ Запуск
bash
Копировать
Редактировать
poetry run python main.py
🧪 Тестирование
bash
Копировать
Редактировать
poetry run pytest
📘 Использование
В main.py создаются продукты и категории:

python
Копировать
Редактировать
product1 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
category1 = Category("Смартфоны", "Описание...", [product1])
Категория автоматически считает:

общее количество созданных продуктов (Category.product_count)

количество созданных категорий (Category.category_count)

🧠 Классы
Product
name: Название товара

description: Описание

price: Цена

quantity: Количество

Category
name: Название категории

description: Описание

products: Список объектов Product

Пример вывода:
Копировать
Редактировать
Смартфоны
Описание...
Количество продуктов: 3
Количество категорий: 2
