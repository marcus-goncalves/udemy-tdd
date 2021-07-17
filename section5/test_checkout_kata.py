"""
Use Cases for Testing
- Can create an instance of Checkout
- Can add an item price
- Can add an item
- Can calculate the total
- Can add multiple items and get correct total
- Can add discount rules
- Can apply discount rules to total
- Exception thrown when item added without price
"""
from .checkout import Checkout


def test_InstantiateCheckout() -> None:
    co = Checkout()


def test_AddItemPrice() -> None:
    co = Checkout()
    co.addItemPrice("a", 1)
