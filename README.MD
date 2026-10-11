🏪 Simple Store Management System
A command-line store management application built with Python using Object-Oriented Programming (OOP) principles.

📋 Overview
This project is a simple store management exercise that simulates a mini retail system. It provides two portals: Manager and Customer. Managers can manage the product inventory, while customers can browse products, add items to a shopping cart, and complete purchases with an automatic invoice generation.

✨ Features
Manager Portal
Add Products – Add new products with name, price, and stock quantity

Find Product – Search for a product by name

List All Products – Display all products currently in the store

Customer Portal
Add to Cart – Add products to the shopping cart (with stock validation)

Remove from Cart – Remove items from the cart

View Cart – Display all items currently in the cart

Checkout – Complete the purchase, generate an invoice, and update product stock

Validation
Product name cannot be empty

Price must be a positive number

Quantity must be a non-negative integer

Stock availability is checked when adding to cart

🗂️ Project Structure
text
simple-store-exercise2/
│
├── main.py          # Entry point – runs the main menu loop
├── store.py         # Store class – manages product inventory
├── product.py       # Product class – represents a store product
├── cart.py          # Cart class – manages customer cart operations
├── cartItem.py      # CartItem class – stores a product with quantity
├── factor.py        # Factor class – generates the final invoice
├── menu.py          # Menu display functions
└── validator.py     # Validator class – handles input validation
🧱 Class Descriptions
Product
Represents a product with name, price, and stock. Uses the Validator class to ensure all attributes are valid.

Store
Manages the list of products. Provides methods to add, find, and list products.

Cart
Handles all cart operations: adding items, removing items, viewing the cart, calculating the total price, and checking out. When checking out, it creates a Factor and updates the product stock accordingly.

CartItem
Represents an item in the cart — a product paired with a quantity. Calculates the total price for that item (price × quantity).

Factor
Stores the list of purchased items and the total price, and formats the final invoice for display.

Validator
A utility class with static methods to validate names, prices, and quantities.

🚀 How to Run
Clone the repository:

bash
git clone https://github.com/zahra-khabar/simple-store-exercise2.git
cd simple-store-exercise2
Run the program:

bash
python main.py
Follow the on-screen menus to interact as a manager or a customer.

🖥️ Usage Example
text
=========================
🛒 MINI STORE MANAGEMENT SYSTEM
=========================
 Welcome! Please select your role:
1. Zahra Khabar_Store_L2-02 Manager
2. Customer
3. Exit Program
Enter your choice: 1
Manager login credentials:

Username: admin

Password: 1234

🛠️ Technologies
Python 3.10+ (uses match statement)

Object-Oriented Programming (Classes, Encapsulation, Static Methods)

No external dependencies – runs entirely on the Python standard library

👩‍💻 Author
Zahra Khabar

This project was created as a practice exercise for Python and OOP logic