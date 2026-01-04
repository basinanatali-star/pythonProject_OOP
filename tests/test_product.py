import pytest

from src.Product import Product
from src.Product import Smartphone
from src.Product import LawnGrass


class TestProduct:
    def test_init(self) -> None:

        product1 = Product(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
        )
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

        assert isinstance(product1, Product)
        assert isinstance(product2, Product)
        assert isinstance(product3, Product)

        assert product1.name == "Samsung Galaxy S23 Ultra"
        assert product1.description == "256GB, Серый цвет, 200MP камера"
        assert product2.price == 210000.0
        assert product3.quantity == 14

    def test_setters(self) -> None:

        product = Product("Телефон", "Смартфон", 5000, 10)

        with pytest.raises(
            ValueError, match="Цена не должна быть нулевая или отрицательная"
        ):
            product.price = 0

        assert product.price == 5000

        with pytest.raises(
            ValueError, match="Цена не должна быть нулевая или отрицательная"
        ):
            product.price = -100

        assert product.price == 5000

        with pytest.raises(ValueError, match="Количество не может быть отрицательным"):
            product.quantity = -100

        assert product.quantity == 10

        with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
            product.quantity = 0

        assert product.quantity == 10

    def test_add(self) -> None:

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
        smartphone1 = Smartphone(
            "Samsung Galaxy S23 Ultra",
            "256GB, Серый цвет, 200MP камера",
            180000.0,
            5,
            95.5,
            "S23 Ultra",
            256,
            "Серый",
        )
        smartphone2 = Smartphone(
            "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
        )
        grass1 = LawnGrass(
            "Газонная трава",
            "Элитная трава для газона",
            500.0,
            20,
            "Россия",
            "7 дней",
            "Зеленый",
        )
        grass2 = LawnGrass(
            "Газонная трава 2",
            "Выносливая трава",
            450.0,
            15,
            "США",
            "5 дней",
            "Темно-зеленый",
        )

        product1.result = 900000.0  # 180000.0 * 5
        product2.result = 1680000.0  # 210000.0 * 8
        product3.result = 434000.0  # 31000.0 * 14
        smartphone1.result = 900000.0  # 180000.0 * 5
        smartphone2.result = 1680000.0  # 210000.0 * 8
        grass1.result = 10000.0  # 500.0 * 20
        grass2.result = 6750.0  # 450.0 * 15

        total_1 = product1 + product2
        assert total_1 == 2580000.0  # 900000.0 + 1680000.0

        total_2 = product2 + product3
        assert total_2 == 2114000.0  # 1680000.0 + 434000.0

        total_3 = smartphone1 + smartphone2
        assert total_3 == 2580000.0

        total_4 = grass1 + grass2
        assert total_4 == 16750.0

        with pytest.raises(TypeError, match="Нельзя складывать объекты разных типов"):
            smartphone1 + grass1

    def test_str(self) -> None:
        product1 = Product(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
        )
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

        assert str(product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
        assert str(product2) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
        assert str(product3) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."


class TestSmartphone:
    def test_init(self) -> None:
        smartphone = Smartphone(
            "Xiaomi Redmi Note 11",
            "1024GB, Синий",
            31000.0,
            14,
            90.3,
            "Note 11",
            1024,
            "Синий",
        )

        assert isinstance(smartphone, Product)
        assert isinstance(smartphone, Smartphone)

        assert smartphone.name == "Xiaomi Redmi Note 11"
        assert smartphone.description == "1024GB, Синий"
        assert smartphone.price == 31000.0
        assert smartphone.quantity == 14
        assert smartphone.efficiency == 90.3
        assert smartphone.model == "Note 11"
        assert smartphone.memory == 1024
        assert smartphone.color == "Синий"


class TestLawnGrass:
    def test_init(self) -> None:
        grass = LawnGrass(
            "Газонная трава",
            "Элитная трава для газона",
            500.0,
            20,
            "Россия",
            "7 дней",
            "Зеленый",
        )

        assert isinstance(grass, Product)
        assert isinstance(grass, LawnGrass)

        assert grass.name == "Газонная трава"
        assert grass.description == "Элитная трава для газона"
        assert grass.price == 500.0
        assert grass.quantity == 20
        assert grass.country == "Россия"
        assert grass.germination_period == "7 дней"
        assert grass.color == "Зеленый"
