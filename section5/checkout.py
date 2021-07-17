"""
Provide a class to:
- Maintains a list of items that are being checked out
- Set the price of individual items
- Add individual items to the checkout
- Total current cost of items in the checkout
- Apply discounts on selected items when N are purchased
"""


class Checkout:
    def __init__(self) -> None:
        self.prices = {}
        self.total = 0

    def addItemPrice(self, item, price) -> None:
        self.prices[item] = price

    def addItem(self, item) -> None:
        self.total += self.prices[item]

    def calculateTotal(self) -> int:
        return self.total
