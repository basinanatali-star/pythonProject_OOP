from src.Category import Category
from src.Product import Product


def test_init() -> None:
    category = Category("Пустая", "Нет товаров", [])

    assert len(category.products) == 0
    assert Category.product_count == 0
    assert Category.category_count == 1

    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и "
        "получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    assert len(category.products) == 3
    assert Category.product_count == 3
    assert Category.category_count == 2
