import pytest

from src.Product import Product


def test_init() -> None:

    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    assert isinstance(product1, Product)
    assert isinstance(product2, Product)
    assert isinstance(product3, Product)

    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product2.price == 210000.0
    assert product3.quantity == 14


def test_setters() -> None:

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

def test_add() -> None:

    product = Product("Телефон", "Смартфон", 5000, 10)
    product.result = 50000

    with pytest.raises(TypeError, match="Можно складывать только объекты Product"):
        product + "не объект"

    with pytest.raises(TypeError, match="Можно складывать только объекты Product"):
        product + 1000

    with pytest.raises(TypeError, match="Можно складывать только объекты Product"):
        product + [1, 2, 3]

    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    product1.result = 900000.0  # 180000.0 * 5
    product2.result = 1680000.0  # 210000.0 * 8
    product3.result = 434000.0  # 31000.0 * 14

    total_1 = product1 + product2
    assert total_1 == 2580000.0 #900000.0 +1680000.0

    total_2 = product2 + product3
    assert total_2 == 2114000.0  # 1680000.0 + 434000.0

def test_str() -> None:
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    assert str(product1) == "Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5"
    assert str(product2) == "Iphone 15, 512GB, Gray space, 210000.0, 8"
    assert str(product3) == "Xiaomi Redmi Note 11, 1024GB, Синий, 31000.0, 14"