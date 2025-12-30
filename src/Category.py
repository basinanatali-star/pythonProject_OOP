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

    def __str__(self):
        return f"Название категории: {self.name}. Kоличество продуктов: {Category.product_count}"

    @property
    def products(self):
        if not self.__products:
            return f"В категории '{self.name}' пока нет товаров"

        products_info = []

        for product in self.__products:
            products_info.append(
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт. "
            )
        return " ".join(products_info)

    @property
    def products_count(self):
        return len(self.__products)

    def add_product(self, product):
        if not isinstance(product, Product):
            raise ValueError("Можно добавлять только объекты Product")
        self.__products.append(product)

        Category.product_count += 1

        return self
