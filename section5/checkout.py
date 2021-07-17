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
        if item not in self.prices:
            raise Exception("Bad Item")
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
            total += self.__calculateItemTotal(item, cnt)
        return total

    def __calculateItemTotal(self, item, cnt) -> int:
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if cnt >= discount.quantity:
                total += self.__calculateItemDiscountedTotal(
                    item, cnt, discount)
            else:
                total += self.prices[item] * cnt
        else:
            total += self.prices[item] * cnt
        return total

    def __calculateItemDiscountedTotal(self, item, cnt, discount) -> int:
        total = 0
        qty_discount = cnt / discount.quantity
        total += qty_discount * discount.price
        remaining = cnt % discount.quantity
        total += remaining * self.prices[item]
        return total
