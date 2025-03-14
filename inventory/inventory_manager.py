import json
import os
from typing import Optional
from inventory.product import Product
from prettytable import PrettyTable
from colorama import Fore, Style, init

init(autoreset=True)  # Ensures colors reset after each print

class InventoryManager:
    """Manages the inventory of products"""

    def __init__(self, filename="inventory.json"):
        """Initialize inventory and load existing data from JSON."""
        self.filename = filename
        self.products = {}  
        self.load_inventory() 

    def load_inventory(self):
        """Loads inventory from a JSON file. If empty, preloads default products."""
        if not os.path.exists(self.filename):
            print(f"⚠️ {self.filename} not found. Initializing with default products.")
            self.preload_default_products()
            return  

        try:
            with open(self.filename, "r") as file:
                data = json.load(file)

            if "products" not in data or not isinstance(data["products"], list):
                print("❌ Invalid JSON format: Missing 'products' key or incorrect format.")
                return

            if not data["products"]:  # If the list is empty, preload products
                print("⚠️ Inventory is empty. Adding default products.")
                self.preload_default_products()
                return

            self.products = {
                item["name"]: Product(
                    item["name"], item["category"], item["price"], item["quantity"]
                )
                for item in data["products"]
            }
            print("✅ Inventory loaded successfully.")

        except json.JSONDecodeError:
            print(f"❌ Error: Invalid JSON format in {self.filename}.")

    def preload_default_products(self):
        """Adds default products to the inventory and saves them."""
        default_products = [
        Product("Shampoo", "Groceries", 5.99, 10),
        Product("Laptop", "Electronics", 999.99, 5),
        Product("T-Shirt", "Clothing", 19.99, 20),
        Product("Desk Lamp", "Home Essentials", 29.99, 8),
        Product("Smartphone", "Electronics", 699.99, 15),
        Product("Headphones", "Electronics", 89.99, 25),
        Product("Running Shoes", "Clothing", 49.99, 12),
        Product("Backpack", "Clothing", 39.99, 18),
        Product("Washing Machine", "Home Essentials", 499.99, 4),
        Product("Refrigerator", "Home Essentials", 799.99, 3),
        Product("Oven", "Home Essentials", 399.99, 5),
        Product("Gaming Mouse", "Electronics", 59.99, 20),
        Product("Office Chair", "Home Essentials", 149.99, 7),
        Product("Notebook", "Groceries", 2.99, 50),
        Product("LED Light Bulb", "Home Essentials", 9.99, 30),
        Product("Coffee Maker", "Home Essentials", 79.99, 6),
        Product("Blender", "Home Essentials", 59.99, 10),
        Product("Towel Set", "Home Essentials", 24.99, 15),
        Product("Yoga Mat", "Clothing", 34.99, 9),
        Product("Hair Dryer", "Home Essentials", 45.99, 11),
        Product("Electric Toothbrush", "Groceries", 39.99, 22),
        Product("Sunscreen", "Groceries", 12.99, 17),
        Product("Printer", "Electronics", 199.99, 6),
        Product("Desk", "Home Essentials", 249.99, 5),
        Product("Speakers", "Electronics", 129.99, 14),
        Product("Fitness Tracker", "Electronics", 149.99, 8),
        Product("Sofa", "Home Essentials", 999.99, 3)
        ]
        
        for product in default_products:
            self.products[product.name] = product
        
        self.save_inventory()
        print("✅ Default products added.")

    def update_price(self, name: str, new_price: float):
        """Updates the price of a product in the inventory."""
        name = name.lower()
        found_product = None

        for product_name in self.products:
            if product_name.lower() == name:
                found_product = product_name
                break

        if found_product:
            self.products[found_product].price = new_price
            self.save_inventory()
            print(f"✅ Price of '{found_product}' updated to {new_price:.2f}€.")
        else:
            print(f"❌ Product '{name}' does not exist.")

    def get_total_inventory_value(self):
        """Calculates the total value of all products in the inventory."""
        total_value = sum(product.price * product.quantity for product in self.products.values())
        return total_value

    def inventory_quantity(self):
        """Calculates the total number of items in inventory."""
        total_quantity = sum(product.quantity for product in self.products.values())
        return total_quantity

    def save_inventory(self):
        """Saves the current inventory to a JSON file."""
        with open(self.filename, "w") as file:
            json.dump(
                {"products": [vars(product) for product in self.products.values()]},
                file,
                indent=4,
            )
        print(f"✅ Inventory saved to {self.filename}")

    def add_product(self, name, category, price, quantity):
        """Add a new product or update quantity if it already exists."""
        if name in self.products:
            print(f"⚠️ Product '{name}' already exists. Increasing quantity by {quantity}.")
            self.products[name].quantity += quantity  # Increment quantity
        else:
            self.products[name] = Product(name, category, price, quantity)

        self.save_inventory()  # ✅ Save after adding

    def remove_product(self, name: str):
        """Removes a product from the inventory (case-insensitive)."""
        name = name.lower()  # Convert input to lowercase
        found_product = None

        for product_name in self.products:
            if product_name.lower() == name:  # Compare case-insensitively
                found_product = product_name
                break

        if found_product:
            del self.products[found_product]
            self.save_inventory()  # ✅ Save after removal
            print(f"✅ Product '{found_product}' removed successfully.")
        else:
            print(f"❌ Product '{name}' does not exist.")


    def update_quantity(self, name: str, new_quantity: int):
        """Updates the quantity of a product in the inventory."""
        if name not in self.products:
            raise ValueError(f"Product '{name}' does not exist.")
        self.products[name].quantity = new_quantity
        self.save_inventory()

    def search_product(self, name: str):
        """Search for a product by name (case-insensitive)."""
        name = name.lower()
        results = [
            product
            for product in self.products.values()
            if product.name.lower() == name
            ]

        if results:
            for product in results:
                print(f"✅ Found: {product.get_product_info()}")
            return results
        else:
            print(f"❌ No product found with name '{name}'.")
            return []
    

    def display_inventory(self):
        """Displays inventory using PrettyTable with colors."""
        if not self.products:
            print(Fore.RED + "📦 Inventory is empty.")
            return

        table = PrettyTable(["Product Name", "Category", "Price (€)", "Quantity"])
        
        category_colors = {
            "Electronics": Fore.CYAN,
            "Clothing": Fore.GREEN,
            "Groceries": Fore.YELLOW,
            "Home Essentials": Fore.MAGENTA
        }

        for product in self.products.values():
            color = category_colors.get(product.category, Fore.WHITE)  # Default to white
            table.add_row([
                color + product.name + Style.RESET_ALL,
                color + product.category + Style.RESET_ALL,
                color + f"{product.price:.2f}€" + Style.RESET_ALL,
                color + str(product.quantity) + Style.RESET_ALL
            ])

        print("\n📦 Inventory:")
        print(table)

