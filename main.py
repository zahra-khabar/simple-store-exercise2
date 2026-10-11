from store import Store
from cart import Cart
from menu import show_main_menu, show_manager_menu, show_customer_menu


store = Store()


while True:

    show_main_menu()
    choice = input("Enter your choice: ")

    match choice:

        # Zahra Khabar_Store_L2-02 Manager
        case "1":
            print("-------------------------")
            print(" Zahra Khabar_Store_L2-02 Manager Login")
            print("-------------------------")

            username = input("Username: ")
            password = input("Password: ")

            if username == "admin" and password == "1234":

                print(" Login successful! Welcome, Manager.")

                while True:

                    show_manager_menu()
                    admin_choice = input("Enter your choice: ")

                    match admin_choice:

                        # Add Product
                        case "1":
                            name = input("Product name: ")
                            price = input("Product price: ")
                            stock = input("Product stock: ")

                            try:
                                product = store.add_product(
                                    name,
                                    price,
                                    stock
                                )

                                print("Product added successfully.")
                                print(product)

                            except ValueError as e:
                                print(f"Error: {e}")

                        # Find Product
                        case "2":
                            name = input("Enter product name: ")

                            try:
                                product = store.find_product(name)
                                print(product)

                            except ValueError as e:
                                print(f"Error: {e}")

                        # List Products
                        case "3":
                            try:
                                store.list_products()

                            except ValueError as e:
                                print(f"Error: {e}")

                        # Return to Main Menu
                        case "4":
                            break

                        case _:
                            print("Invalid choice.")

            else:
                print(" Invalid username or password.")

        # Customer
        case "2":

            cart = Cart()

            while True:

                show_customer_menu()
                customer_choice = input("Enter your choice: ")

                match customer_choice:

                    # Add item
                    case "1":
                        product_name = input("Product name: ")
                        quantity = input("Quantity: ")

                        try:
                            product = store.find_product(product_name)

                            cart.add_to_cart(
                                product,
                                int(quantity)
                            )

                            print(" Product added to cart.")

                        except ValueError as e:
                            print(f"Error: {e}")

                    # Remove item
                    case "2":
                        product_name = input("Product name: ")

                        try:
                            cart.remove_from_cart(product_name)
                            print(" Product removed from cart.")

                        except ValueError as e:
                            print(f"Error: {e}")

                    # View cart
                    case "3":
                        cart.view_cart()

                    # Checkout
                    case "4":
                        try:
                            cart.checkout()

                        except ValueError as e:
                            print(f"Error: {e}")

                    # Return to main menu
                    case "5":
                        break

                    case _:
                        print("Invalid choice.")

        # Exit
        case "3":
            print("Goodbye!")
            break

        case _:
            print("Invalid choice.")