"""
Provide a class to:
- Maintains a list of items that are being checked out
- Set the price of individual items
- Add individual items to the checkout
- Total current cost of items in the checkout
- Apply discounts on selected items when N are purchased
"""


class Checkout:
    class Discount:
        def __init__(self, quantity, price) -> None:
            self.quantity = quantity
            self.price = price

    def __init__(self) -> None:
        self.prices = {}
        self.discounts = {}
        self.items = {}
        self.total = 0

    def addItemPrice(self, item, price) -> None:
        self.prices[item] = price

    def addItem(self, item) -> None:
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def addDiscount(self, item, quantity, price) -> None:
        discount = self.Discount(quantity, price)
        self.discounts[item] = discount

    def calculateTotal(self) -> int:
        total = 0
        for item, cnt in self.items.items():
            total += self.prices[item] * cnt
        return total
