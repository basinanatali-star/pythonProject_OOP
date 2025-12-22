class Product:
    name: str
    description: str
    __price: float
    __quantity: int

    product_count = 0

    def __init__(self, name, description, price, quantity):

        if price <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным")

        self.name = name
        self.description = description
        self.__price = price
        self.__quantity = quantity

        Product.product_count += 1

    @classmethod
    def new_product(cls, product_data):
        """Класс-метод для создания объекта из словаря"""
        return cls(**product_data)

    @property
    def price(self) -> float:
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, value: float):
        """Сеттер для цены с проверкой"""
        if value <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        self.__price = value

    @property
    def quantity(self) -> int:
        """Геттер для количества"""
        return self.__quantity

    @quantity.setter
    def quantity(self, value: int):
        """Сеттер для количества с проверкой"""
        if value < 0:
            raise ValueError("Количество не может быть отрицательным")
        self.__quantity = value
