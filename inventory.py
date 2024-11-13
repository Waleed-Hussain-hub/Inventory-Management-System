# inventory.py



class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product

    def update_product(self, product_id, **updates):
        product = self.products.get(product_id)
        if not product:
            print("Product not found")
            return
        for key, value in updates.items():
            if hasattr(product, key):
                setattr(product, key, value)

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
        else:
            print("Product not found")

    def view_products(self):
        for product in self.products.values():
            print(product)

    def check_stock_levels(self, threshold=5):
        for product in self.products.values():
            if product.stock_quantity <= threshold:
                print(f"Low stock alert for {product.name}. Please restock soon.")
