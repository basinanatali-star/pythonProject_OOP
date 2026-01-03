from src.Product import Product


def test_print_mixin():
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product2.description == "Фоновая подсветка"
    assert product1.price == 180000.0
    assert product2.quantity == 7
