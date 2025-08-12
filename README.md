
---

## 🔑 Основная функциональность

### 1. **Абстрактный базовый класс**
- `BaseProduct` — общий интерфейс для всех товаров.
- Определяет обязательные атрибуты (`name`, `description`, `price`, `quantity`) и методы (`__add__`).
- Реализует геттер/сеттер для цены с проверкой на положительное значение.

### 2. **Класс-миксин**
- `InfoMixin` выводит в консоль сообщение при создании объекта с указанием класса и параметров.

### 3. **Классы товаров**
- `Product` — базовый класс товара, наследует `BaseProduct` и `InfoMixin`.
- `Smartphone` — расширяет `Product` атрибутами:
  - `efficiency`, `model`, `memory`, `color`.
- `LawnGrass` — расширяет `Product` атрибутами:
  - `country`, `germination_period`, `color`.
- Возможность сложения (`__add__`) только для объектов одного типа, иначе `TypeError`.
- Класс-метод `new_product()` для создания объекта из словаря.

### 4. **Категории**
- `Category`:
  - Считает количество категорий и товаров.
  - Список товаров хранится в приватном атрибуте `__products`.
  - Метод `add_product()` принимает только объекты `Product` или его наследников.
  - Свойство `products` возвращает список строк в формате:
    ```
    Название, Цена руб. Остаток: N шт.
    ```

---

## 🚀 Пример использования
```python
from src.product import Smartphone, LawnGrass
from src.category import Category

smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")
smartphone2 = Smartphone("iPhone 15", "512GB, Gray", 210000.0, 8, 98.2, "15", 512, "Gray")

grass1 = LawnGrass("Газонная трава", "Элитная", 500.0, 20, "Россия", "7 дней", "Зеленый")

category_smartphones = Category("Смартфоны", "Флагманы", [smartphone1, smartphone2])
category_grass = Category("Газонная трава", "Разные виды", [grass1])

print(category_smartphones.products)
print(category_grass.products)
