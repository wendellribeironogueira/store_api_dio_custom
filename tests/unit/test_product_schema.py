from app.schemas.product_schema import Product

def test_valid_product():
    product = Product(name="Camisa", price=49.9, quantity=10)
    assert product.name == "Camisa"
    assert product.price == 49.9
    assert product.quantity == 10