from validator import *

class Product:
    """This class Describe a product in the store."""

    def __init__(self, name: str, price: float, stock: int):
        self.name = Validator.validate_name(name)
        self.price = Validator.validate_price(price)
        self.stock = Validator.validate_quantity(stock)


    def __str__(self):
        return(
            f'product: {self.name} - price: {self.price}$ , stock: {self.stock}'
        )
