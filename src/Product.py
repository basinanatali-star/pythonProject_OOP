from src.print_mixin import PrintMixin

from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass


class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    __price: float
    __quantity: int

    product_count = 0
    total_quantity = 0
    result = 0.0

    def __init__(self, name, description, price, quantity):

        if price <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным")
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        self.name = name
        self.description = description
        self.__price = price
        self.__quantity = quantity
        super().__init__()

        Product.product_count += 1

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты Product")

        if type(self) is not type(other):
            raise TypeError("Нельзя складывать объекты разных типов")

        result = self.__price * self.__quantity + other.__price * other.__quantity

        return result

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.__quantity} шт."

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
        if value == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.__quantity = value


class Smartphone(Product):
    name: str
    description: str
    __price: float
    __quantity: int
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    name: str
    description: str
    __price: float
    __quantity: int
    country: str
    germination_period: str
    color: str

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
