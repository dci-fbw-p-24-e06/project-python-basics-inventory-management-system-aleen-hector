import json
from typing import Optional
from inventory.product import Product
from prettytable import PrettyTable
from colorama import Fore, Style, init

init(autoreset=True)  # Ensures colors reset after each print


class InventoryManager:
    """Manages the inventory of products"""

    def __init__(self):
        self.products = {}  # Dictionary to store products

    def load_from_json(self, filename):
        """Load inventory data from a JSON file."""
        try:
            with open(filename, "r") as file:
                data = json.load(file)

            if "products" not in data or not isinstance(data["products"], list):
                print("❌ Invalid format in JSON: missing 'products' key or incorrect format")
                return

            for item in data["products"]:
                self.add_product(
                    item["name"], item["category"], item["price"], item["quantity"]
                )

            print("✅ Inventory loaded successfully.")

        except FileNotFoundError:
            print(f"❌ Error: {filename} not found.")
        except json.JSONDecodeError:
            print(f"❌ Error: Invalid JSON format in {filename}.")

    def add_product(self, name: str, category: str, price: float, quantity: int) -> None:
        """Add a new product to the inventory."""
        if name in self.products:
            raise ValueError(f"Product {name} already exists")
        self.products[name] = Product(name, category, price, quantity)

    def remove_product(self, name: str) -> None:
        """Removes a product from the inventory."""
        if name not in self.products:
            raise ValueError(f"Product {name} does not exist")
        del self.products[name]

    def update_quantity(self, name: str, new_quantity: int) -> None:
        """Updates the quantity of a product in the inventory."""
        if name not in self.products:
            raise ValueError(f"Product {name} does not exist")
        self.products[name].quantity = new_quantity

    def decrease_quantity(self, name: str, quantity: int) -> int:
        """Decreases the quantity of a product in the stock."""
        if name not in self.products:
            raise ValueError(f"Product {name} does not exist.")
        return self.products[name].decrease_quantity(quantity)

    def update_price(self, name: str, new_price: float) -> None:
        """Update the price of the product."""
        if name not in self.products:
            raise ValueError(f"Product {name} does not exist.")
        self.products[name].price = new_price

    def retrieve_product_information(self, name: str) -> str:
        """Retrieve product information."""
        if name not in self.products:
            raise ValueError(f"Product {name} does not exist.")
        return self.products[name].get_product_info()

    def inventory_info(self, product_name: str) -> str:
        """Check inventory status of a product and return relevant information."""
        if product_name not in self.products:
            return f"Product {product_name} does not exist in the inventory"

        product = self.products[product_name]
        info = product.get_inventory_info()

        if product.quantity == 5:
            return f"{info}\n⚠️ Warning: {product_name} is low on stock! Only {product.quantity} left."
        if product.quantity == 0:
            return f"{info}\n❌ {product_name} is out of stock!"

    def get_total_inventory_value(self) -> float:
        """Calculate and return the total value of all products in the inventory."""
        return sum(product.calculate_total_value() for product in self.products.values())

    def get_product(self, product_name: str) -> Optional[Product]:
        """Retrieves a product by name."""
        return self.products.get(product_name)

    def inventory_value(self) -> float:
        """Calculate and return the total value of all products in the inventory."""
        return sum(product.calculate_total_value() for product in self.products.values())

    def inventory_quantity(self) -> int:
        """Calculate and return the total quantity in the inventory."""
        return sum(product.quantity for product in self.products.values())

    def save_inventory(self, filename: str) -> None:
        """Save the current inventory to a JSON file."""
        with open(filename, "w") as file:
            json.dump(
                {"products": [vars(product) for product in self.products.values()]},
                file,
                indent=4,
            )
        print(f"Inventory saved to {filename}")

    def display_inventory(self) -> None:
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

