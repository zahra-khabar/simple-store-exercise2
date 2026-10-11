class Factor:
    """Stores and displays the final purchase invoice in this class!"""

    def __init__(self, items, total_price):
        self.items = items
        self.total_price = total_price

    def __str__(self):
        result = "========== Factor ==========\n"
        for item in self.items:
            result += f"{item}\n"
        result += f"Total Price: {self.total_price:.2f}\n"
        result += "============================="

        return result