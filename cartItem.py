from product import Product
from validator import *


class CartItem():
    """This Class stores the cart item with total price for each product """

    def __init__(self,product: Product, quantity: int) :
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.product = product
        self.quantity = Validator.validate_quantity(quantity)

    def calculate_total_price(self):
        total_price = self.product.price * self.quantity
        return total_price

    def __str__(self):
        return (
            f"{self.product.name} | "
            f"Quantity: {self.quantity} | "
            f"{self.calculate_total_price()}"
        )