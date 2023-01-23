import pytest
from ShoppingCart.shopping_cart import ShoppingCart


@pytest.fixture
def car():
    return ShoppingCart(5)

@pytest.mark.parametrize("x,y,z",[("banana" , "apple", "pitch")])
def test_add_item(car, x, y, z):
    car.add(x)
    car.add(y)
    car.add(z)
    assert car.size() == 3


@pytest.mark.one #one is the name
def test_item_in_cart(car):
    car.add('banana')
    assert "banana" in car.get_items()


def test_adding_more_than_max(car):
    for i in range(5):
        car.add('orange')

    with pytest.raises(OverflowError):
        car.add('apple')

