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
    co = Checkout()
    co.addItemPrice("a", 1)
    co.addItemPrice("b", 2)
    return co


def test_CalculateTotal(checkout) -> None:
    checkout.addItem("a")
    assert checkout.calculateTotal() == 1


def test_CalculateTotalWithMultipleItems(checkout) -> None:
    checkout.addItem("a")
    checkout.addItem("b")
    assert checkout.calculateTotal() == 3


def test_ApplyDiscount(checkout) -> None:
    checkout.addDiscount("a", 3, 2)


@pytest.mark.skip
def test_AddDiscountRule(checkout) -> None:
    checkout.addDiscount("a", 3, 2)
    checkout.addItem("a")
    checkout.addItem("a")
    checkout.addItem("a")
    assert checkout.calculateTotal() == 2
