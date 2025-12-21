from src.Product import Product


class Category:
    name: str
    description: str
    __products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = []

        if products:
            for product in products:
                self.add_product(product)
        Category.category_count += 1

    def add_product(self, product):
        if not isinstance(product, Product):
            raise ValueError("Можно добавлять только объекты Product")
        self.__products.append(product)
        Category.product_count += 1
        return self

    @property
    def products(self):
        return self.__products.copy()
