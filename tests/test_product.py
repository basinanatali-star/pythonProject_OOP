import pytest

from src.Product import Product


def test_init() -> None:
    try:
        product1 = Product(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
        )
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

        print(product1)
        print(product2)
        print(product3)

    except ValueError as e:
        print(f"Ошибка: {e}")

def test_new_product() -> None:

    product = Product("Телефон", "Смартфон", 5000, 10)

    with pytest.raises(ValueError, match="Цена не должна быть нулевая или отрицательная"):
        product.price = 0

    assert product.price == 5000

    with pytest.raises(ValueError, match="Цена не должна быть нулевая или отрицательная"):
        product.price = -100

    assert product.price == 5000

    with pytest.raises(ValueError, match="Количество не может быть отрицательным"):
        product.quantity = -100

    assert product.quantity == 10