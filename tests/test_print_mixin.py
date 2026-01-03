from src.Product import Product
from src.Product import LawnGrass


def test_print_mixin():
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    grass1 = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )

    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product2.description == "Фоновая подсветка"
    assert product1.price == 180000.0
    assert product2.quantity == 7
    assert grass1.name == "Газонная трава"
    assert grass1.color == "Зеленый"
