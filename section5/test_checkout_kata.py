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
import pytest
from .checkout import Checkout


@pytest.fixture()
def checkout() -> Checkout:
    return Checkout()


def test_AddItemPrice(checkout) -> None:
    checkout.addItemPrice("a", 1)


def test_AddItem(checkout) -> None:
    checkout.addItem("a")


def test_CalculateTotal(checkout) -> None:
    checkout.addItemPrice("a", 1)
    checkout.addItem("a")
    assert checkout.calculateTotal() == 1


def test_CalculateTotalWithMultipleItems(checkout) -> None:
    checkout.addItemPrice("a", 1)
    checkout.addItemPrice("b", 2)
    checkout.addItem("a")
    checkout.addItem("b")
    assert checkout.calculateTotal() == 3
