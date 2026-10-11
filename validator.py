class Validator:
    """"This Class is used to checking our general Validation for Name, Price & Quantity"""

    @staticmethod
    def validate_name(name):
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        return name

    @staticmethod
    def validate_price(price):
        try:
            price = float(price)
            if price < 0:
                raise ValueError(
                    f"{price} Must be a positive number."
                )
        except ValueError:
            raise ValueError(
                f"{price} is not a valid price."
            )
        return price

    @staticmethod
    def validate_quantity(quantity):
        try:
            quantity = int(quantity)
            if quantity < 0:
                raise ValueError(
                    f"{quantity} Must be a positive number."
                )
        except ValueError:
            raise ValueError(
                f"Invalid quantity: {quantity}"
            )
        return quantity
