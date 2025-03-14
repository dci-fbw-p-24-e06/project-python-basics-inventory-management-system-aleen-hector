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
        """Loads inventory from a JSON file if it exists."""
        if not os.path.exists(self.filename):
            print(f"⚠️ {self.filename} not found. Initializing empty inventory.")
            return  # Avoid crashing if file doesn't exist

        try:
            with open(self.filename, "r") as file:
                data = json.load(file)

            if "products" not in data or not isinstance(data["products"], list):
                print("❌ Invalid JSON format: Missing 'products' key or incorrect format.")
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
        """Removes a product from the inventory."""
        if name not in self.products:
            raise ValueError(f"Product '{name}' does not exist.")
        del self.products[name]
        self.save_inventory()  # ✅ Save after removal

    def update_quantity(self, name: str, new_quantity: int):
        """Updates the quantity of a product in the inventory."""
        if name not in self.products:
            raise ValueError(f"Product '{name}' does not exist.")
        self.products[name].quantity = new_quantity
        self.save_inventory()  # ✅ Save after update

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

