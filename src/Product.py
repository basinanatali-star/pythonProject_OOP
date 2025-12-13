class Product:
    name: str
    description: str
    price: float
    quantity: int

    product_count = 0

    def __init__(self, name, description, price, quantity):

        if price <= 0:
            raise ValueError("Цена должна быть положительным числом")
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным")

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

        Product.product_count += 1
