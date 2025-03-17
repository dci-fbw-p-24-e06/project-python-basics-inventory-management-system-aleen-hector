import json
import os
from inventory.product import Product
from prettytable import PrettyTable
from colorama import Fore, Style, init
import time
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.style import Style

console = Console()


init(autoreset=True)  # Ensures colors reset after each print


class InventoryManager:
    """Manages the inventory of products"""

    def __init__(self, filename="inventory.json", test_mode=False):
        """Initialize inventory and load existing data from JSON."""
        self.filename = filename
        self.products = {}  
        self.test_mode = test_mode  # New parameter to avoid auto-saving in tests
        self.load_inventory()

    def clear_inventory(self):
        self.products.clear()

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
        """Saves the current inventory to a JSON file, unless in test mode."""
        if not self.test_mode:  # Skip saving if we're in test mode
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
            print(f"⚠️ Product '{name}' already exists with quantity {self.products[name].quantity}.")
            choice = input("Do you want to update the quantity? (yes/no): ").strip().lower()
            
            if choice in ['y', 'yes']:
                new_quantity = input("Enter new quantity (additive, e.g., +5 or -3): ").strip()
                
                if new_quantity.startswith('+') or new_quantity.startswith('-'):
                    try:
                        self.products[name].quantity += int(new_quantity)
                        print(f"✅ Updated '{name}' quantity to {self.products[name].quantity}.")
                    except ValueError:
                        print("❌ Invalid input. Quantity remains unchanged.")
                else:
                    try:
                        self.products[name].quantity = int(new_quantity)
                        print(f"✅ Set '{name}' quantity to {self.products[name].quantity}.")
                    except ValueError:
                        print("❌ Invalid input. Quantity remains unchanged.")
                
                self.save_inventory()  # Save the updated quantity
            else:
                print("ℹ️ No changes made to the existing product.")
        else:
            self.products[name] = Product(name, category, price, quantity)
            self.save_inventory()  # Save after adding
            print(f"✅ Added new product '{name}' with quantity {quantity}.")


    def remove_product(self, name: str):
        """Removes a product from the inventory (case-insensitive) or prints a message if not found."""
        name = name.lower()  # Convert input to lowercase
        found_product = None

        for product_name in self.products:
            if product_name.lower() == name:  # Compare case-insensitively
                found_product = product_name
                break

        if found_product:
            del self.products[found_product]
            self.save_inventory()  # Save after removal
            print(f"✅ Product '{found_product}' removed successfully.")
        else:
            print(f"ℹ️ Product '{name}' does not exist. Nothing to remove.")  # Instead of raising an error



    def update_quantity(self, name, new_quantity):
        """Update the quantity of an existing product in a case-insensitive manner.
        In test mode, raises a ValueError if the product does not exist."""
        # Find the product key using a case-insensitive search.
        product_key = None
        for key in self.products:
            if key.lower() == name.lower():
                product_key = key
                break

        if product_key is not None:
            try:
                new_quantity = int(new_quantity)
                self.products[product_key].quantity = new_quantity
                self.save_inventory()
                print(f"✅ Updated '{product_key}' quantity to {new_quantity}.")
            except ValueError:
                print("❌ Invalid quantity. Please enter a valid number.")
        else:
            # In test mode, immediately raise a ValueError.
            if self.test_mode:
                raise ValueError(f"Product '{name}' does not exist.")
            else:
                print(f"🙋 Product '{name}' does not exist. Nothing to update.")
                choice = input("Do you want to add the product to your inventory? (yes/no): ").strip().lower()
                if choice in ['y', 'yes']:
                    category = input("Enter category: ").strip()
                    price = float(input("Enter price (€): ").strip())
                    try:
                        new_quantity = int(new_quantity)
                    except ValueError:
                        print("❌ Invalid quantity. Please enter a valid number.")
                        return
                    # Add the new product using the provided name.
                    self.products[name] = Product(name, category, price, new_quantity)
                    self.save_inventory()
                    print(f"✅ Added new product '{name}' with quantity {new_quantity}.")


    def search_product(self, name):
        """Search for a product by name with a loading animation and low-stock warning.
        Always returns a list of found products (even if empty)."""
        name = name.lower()
        found_products = []

        # Animated progress bar
        with Progress(
            SpinnerColumn(),        # Loading spinner
            TextColumn("[cyan]Searching...[/]"),  # Text animation
            BarColumn(),            # Loading bar
            transient=True          # Hides after completion
        ) as progress:
            task = progress.add_task("", total=100)
            for _ in range(10):  # Simulating a delay
                time.sleep(0.1)
                progress.update(task, advance=10)
            
            # Perform case-insensitive search
            for product in self.products.values():
                if name in product.name.lower():
                    found_products.append(product)

        # Display results
        if found_products:
            console.print(f"✅ [green]Found {len(found_products)} result(s):[/]")
            for product in found_products:
                stock_warning = ""
                if product.quantity < 3:
                    stock_warning = " ⚠️ [bold red](Low stock!)[/]"
                console.print(
                    f"📦 [cyan]{product.name}[/] - 🏷️ [yellow]{product.category}[/] - "
                    f"💰 [green]{product.price}€[/] - 📦 [blue]{product.quantity} in stock[/]{stock_warning}"
                )
        else:
            console.print(f"❌ [red]No product found with name '{name}'.[/]")

        # Always return the list (even if empty)
        return found_products



    def display_inventory(self):
        """Display inventory with Rich tables."""
        table = Table(title="💁 Inventory", show_lines=True)

        table.add_column("Product Name", style="cyan")
        table.add_column("Category", style="magenta")
        table.add_column("Price (€)", style="green")
        table.add_column("Quantity", style="yellow")

        for product in self.products.values():
            table.add_row(product.name, product.category, f"{product.price:.2f}€", str(product.quantity))

        console.print(table)
