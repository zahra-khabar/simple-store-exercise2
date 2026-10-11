from cartItem import CartItem
from factor import Factor

class Cart:
    """Manages customer cart operations and checkout."""
    def __init__(self):
        self.cart_items = list()

    def add_to_cart(self, product, quantity):
        for item in self.cart_items:
            if item.product == product:
                new_quantity = item.quantity + quantity
                if new_quantity > product.stock:
                    raise ValueError(
                        f"Not enough stock for {product.name}.")
                item.quantity = new_quantity
                return self.cart_items

        if quantity > product.stock:
            raise ValueError(
                f"Not enough stock for {product.name}.")

        cart_item = CartItem(product, quantity)
        self.cart_items.append(cart_item)
        return self.cart_items


    def remove_from_cart(self, product_name):
        for item in self.cart_items:
            if item.product.name.lower() == product_name.lower():
                self.cart_items.remove(item)
                return self.cart_items
        raise ValueError("Product not found in cart.")

    def view_cart(self):
        if len(self.cart_items) == 0:
            print("No items added.")
            return
        for item in self.cart_items:
            print(item)

    def total_price(self):
        totals = 0
        for cart_item in self.cart_items:
            totals += cart_item.calculate_total_price()
        return totals

    def checkout(self):
        if not self.cart_items:
            raise ValueError("Cart is empty.")

        total = self.total_price()
        for item in self.cart_items:
            item.product.stock -= item.quantity
        factor = Factor(self.cart_items.copy(), total)
        print(factor)
        self.cart_items.clear()

        return factor