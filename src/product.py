class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = new_price

    @classmethod
    def new_product(cls, product_dict: dict) -> "Product":
        """
        Создание нового объекта Product из словаря
        """
        return cls(
            name=product_dict.get("name", ""),
            description=product_dict.get("description", ""),
            price=product_dict.get("price", 0),
            quantity=product_dict.get("quantity", 0),
        )
