from product import Product


class Store:
    """This class is related to the manager portal for the store."""

    def __init__(self):
        self.products = list()

    def find_product(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None

    def list_products(self):
        if not self.products:
            print("No products available in the store.")
            return
        for product in self.products:
            print(product)

    def add_product(self, name, price, stock):
        # First, we check if the product exists in the store
        if self.find_product(name):
            raise ValueError(
                "Product exists. Try to add another product name."
            )
        product = Product(name, price, stock)
        self.products.append(product)
        return product

