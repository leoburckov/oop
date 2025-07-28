class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            raise ValueError("Цена не должна быть нулевой или отрицательной")
        self.__price = new_price

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
