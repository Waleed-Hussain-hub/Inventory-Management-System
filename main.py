# main.py

from user_management import AuthSystem
from inventory import Inventory
from product import Product

def main():
    auth_system = AuthSystem()
    inventory = Inventory()

    # Adding initial products to the inventory
    initial_products = [
        Product("001", "Sweet", "Dessert", 5.00, 10),
        Product("002", "Bread", "Bakery", 2.50, 20),
        Product("003", "Donuts", "Dessert", 1.50, 15),
        Product("004", "Cake", "Dessert", 10.00, 5),
        Product("005", "Pastries", "Bakery", 3.00, 8),
        Product("006", "Muffins", "Bakery", 2.00, 12)
    ]

    for product in initial_products:
        inventory.add_product(product)

    # Prompt for username and password
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    # Perform login
    user = auth_system.login(username, password)

    if user:
        if user.role == 'Admin':
            while True:
                print("Admin options: 1- Add Product, 2- Update Product, 3- Delete Product, 4- View Products, 5- Exit")
                choice = input("Choose an option: ")

                if choice == '1':
                    # Adding product
                    product_id = input("Enter product ID: ")
                    name = input("Enter product name: ")
                    category = input("Enter product category: ")
                    price = float(input("Enter product price: "))
                    stock_quantity = int(input("Enter stock quantity: "))
                    product = Product(product_id, name, category, price, stock_quantity)
                    inventory.add_product(product)

                elif choice == '2':
                    # Updating product
                    product_id = input("Enter product ID to update: ")
                    name = input("Enter new name (or leave blank to skip): ")
                    category = input("Enter new category (or leave blank to skip): ")
                    price = input("Enter new price (or leave blank to skip): ")
                    stock_quantity = input("Enter new stock quantity (or leave blank to skip): ")

                    updates = {}
                    if name: updates["name"] = name
                    if category: updates["category"] = category
                    if price: updates["price"] = float(price)
                    if stock_quantity: updates["stock_quantity"] = int(stock_quantity)
                    inventory.update_product(product_id, **updates)

                elif choice == '3':
                    # Deleting product
                    product_id = input("Enter product ID to delete: ")
                    inventory.delete_product(product_id)

                elif choice == '4':
                    # Viewing products with stock info (Admin only)
                    for product in inventory.products.values():
                        print(f"{product.product_id} - {product.name} - ${product.price} - Stock: {product.stock_quantity}")

                elif choice == '5':
                    print("Exiting Admin panel.")
                    break

                else:
                    print("Invalid option, try again.")

        elif user.role == 'User':
            print("Welcome, User! Here are the available products:")
            # Viewing products without stock info (User only)
            for product in inventory.products.values():
                print(f"{product.name} - ${product.price}")

            # Shopping cart for selected products
            cart = []
            while True:
                print("\nEnter product name to add to your cart, or type 'finish' to complete your selection:")
                product_name = input("Product name or 'finish': ")

                if product_name.lower() == 'finish':
                    # Calculate the bill with a 7% sales tax
                    subtotal = sum(item['product'].price * item['quantity'] for item in cart)
                    tax = subtotal * 0.07
                    total = subtotal + tax

                    # Display bill summary
                    print("\n--- Bill Summary ---")
                    for item in cart:
                        print(f"{item['quantity']} x {item['product'].name} - ${item['product'].price * item['quantity']:.2f}")
                    print(f"Subtotal: ${subtotal:.2f}")
                    print(f"Sales Tax (7%): ${tax:.2f}")
                    print(f"Total: ${total:.2f}")
                    print("\nThank you for shopping with us!")
                    break

                else:
                    # Add selected product to cart based on name
                    product = next((p for p in inventory.products.values() if p.name.lower() == product_name.lower()), None)
                    if product:
                        # Ask for quantity and update stock if available
                        while True:
                            try:
                                quantity = int(input(f"Enter quantity for {product.name}: "))
                                if quantity > product.stock_quantity:
                                    print(f"Sorry, only {product.stock_quantity} available. Try a lower quantity.")
                                else:
                                    # Add to cart and reduce stock
                                    cart.append({"product": product, "quantity": quantity})
                                    product.stock_quantity -= quantity
                                    print(f"{quantity} x {product.name} added to your cart.")
                                    break
                            except ValueError:
                                print("Invalid quantity. Please enter a number.")
                    else:
                        print("Product not found. Please try again.")
    else:
        print("Access denied")

if __name__ == "__main__":
    main()
class AuthSystem:
    def login(self, username, password):
        if username == 'Waleed' and password == 'Waleed12345':
            return User(username, 'Admin')
        elif username == 'user' and password == 'user123':
            return User(username, 'User')
        else:
            return None
