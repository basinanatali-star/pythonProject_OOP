import pytest

from src.Category import Category
from src.Product import Product


@pytest.fixture(autouse=True)
def reset_counters():
    Category.category_count = 0
    Category.product_count = 0
    Product.product_count = 0
    yield

def test_init() -> None:
    category_1 = Category("Пустая", "Нет товаров", [])

    assert category_1.products_count == 0
    assert Category.product_count == 0
    assert Category.category_count == 1

    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category_2 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и "
        "получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    assert category_2.products_count == 3
    assert Category.product_count == 3
    assert Category.category_count == 2

def test_add_product() -> None:
    category = Category("Книги", "Литература", [])

    with pytest.raises(ValueError, match="Можно добавлять только объекты Product"):
        category.add_product("Не товар")

    assert category.products_count == 0

    valid_product = Product("Книга", "Интересная", 500, 10)
    category.add_product(valid_product)

    assert category.products_count == 1

def test_str() -> None:
    category_3 = Category("Автомобили", "Нет товаров", [])
    result = str(category_3)
    assert result == "Название категории: Автомобили. Kоличество продуктов: 0"

    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    category = Category("Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и "
        "получения дополнительных функций для удобства жизни",
        [product1]
    )
    result = str(category)
    assert result == "Название категории: Смартфоны. Kоличество продуктов: 1"
