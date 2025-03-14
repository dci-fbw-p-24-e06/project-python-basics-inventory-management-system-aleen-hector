import json
from typing import Optional
from inventory.product import Product


class InventoryManager:
    """Manages the inventory of products"""

    def __init__(self):
        """Initialize an empty inventory"""
        self.products = {}

    def add_product(
        self, name: str, category: str, price: float, quantity: int
    ) -> None:
        """
        Add a new product to the inventory.
        Parameters:
        name (str): Name of the product
        category (str): Category of the product.
        price (float): Price of the product in euros.
        quantity (int): Initial quantity of the product.
        raises ValueError: If product is already in the inventory.
        """
        if name in self.products:
            raise ValueError(f"Product {name} already exists")
        self.products[name] = Product(name, category, price, quantity)

    def remove_product(self, name: str) -> None:
        """
        Removes a product from the inventory.
        Parameters:
        name (str): Name of the product to remove.
        raises ValueError: If product does not exist.
        """
        if name not in self.products:
            raise ValueError(f"Product {name} does not exist")
        del self.products[name]

    def update_quantity(self, name: str, new_quantity: int) -> int:
        """
        Updates the quantity of a product in the inventory.
        Parameters:
        name (str): Name of the product to update.
        new_quantity (int): New quantity for the product.
        raises ValueError: If product does not exist.
        """
        if name not in self.products:
            raise ValueError(f"Product {name} does not exist")
        self.products[name].quantity = new_quantity

    def decrease_quantity(self, name: str, quantity: int) -> int:
        """
        Decreases the quantity of a product in the stock.
        Parameters:
        name (str): Name of the product to update.
        quantity (int): Amount to decrease from stock."
        raises ValueError: If the product does not exist.
        returns (int): Updated quantity of the product.
        """
        if name not in self.products:
            raise ValueError(f"Product {name} does not exist.")
        return self.products[name].decrease_quantity(quantity)

    def update_price(self, name: str, new_price: float) -> None:
        """Update the price of the product.
        Parameters:
        name (str): Name of the product to update.
        new_price (float): New price for the product.
        raises ValueError: If product does not exist.
        """
        if name not in self.products:
            raise ValueError(f"Product {name} does not exist.")
        self.products[name].price = new_price

    def retrieve_product_information(self, name):
        """
        Retrieve product information.
        Parameters:
        name (str): Name of the product.
        raises ValueError: If product does not exist.
        returns (str): Product information.
        """
        if name not in self.products:
            raise ValueError(f"Product {name} does not exist.")
        return self.products[name].get_product_info()

    def inventory_info(self, product_name: str) -> str:
        """
        Check inventory status of a product and return relevant information.
        Parameters:
        product_name (str): Name of the product.
        raises ValueError: If product does not exist.
        returns (str): Inventory information.
        """
        if product_name not in self.products:
            return f"Product {product_name} does not exist in the inventory"

        product = self.products[product_name]
        info = product.get_inventory_info()

        if product.quantity == 5:
            return (
                f"{info}\n⚠️ Warning: {product_name} is low on stock!"
                f"Only {product.quantity} left."
            )
        if product.quantity == 0:
            return f"{info}\n❌ {product_name} is out of stock!"

    def get_total_inventory_value(self) -> float:
        """
        Calculate and return the total value of all products in the inventory.
        returns (float): Total inventory value.
        """
        total_value = 0
        for product in self.products.values():
            total_value += product.calculate_total_value()
        return total_value

    def get_product(self, product_name: str) -> Optional[Product]:
        """
        Retrieves a product by name.
        Parameters:
        product_name (str): Name of the product.
        returns (str): The product if found, None otherwise.
        """
        return self.products.get(product_name)

    def inventory_value(self) -> float:
        """
        Calculate and return the total value of all products in the inventory.
        returns (float): Total inventory value (price * quantity)
        """
        return sum(
            product.calculate_total_value() for product in self.products.values()
        )

    def inventory_quantity(self) -> int:
        """
        Calculate and return the total quantity of all products in the inventory.
        returns (int): Total inventory quantity
        """
        return sum(product.quantity for product in self.products.values())
        return sum(
            product.price * product.quantity for product in self.products.values()
        )

    def save_inventory(self, filename: str) -> None:
        """
        Save the current inventory to a JSON file.
        Parameters:
        filename (str): Name of the JSON file to save.
        """
        with open(filename, "w") as file:
            json.dump(
                {name: vars(product) for name, product in self.products.items()},
                file,
                indent=4,
            )

            print(f"Inventory saved to {filename}")

    def load_from_json(self, file_path: str) -> None:
        """
        Load inventory data from a JSON file.
        Parameters:
        file_path (str): Path to the JSON file to load.
        """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for item in data:
                    self.add_product(
                        name=item.get("name"),
                        category=item.get("category"),
                        price=item.get("price"),
                        quantity=item.get("quantity"),
                    )
            print(f'Product {item.get("name")} loaded from JSON.')
            print(f"Inventory now has {len(self.products)} products.")
            print(f"Total inventory value: {self.get_total_inventory_value():.2f} €")
            print(f"Total inventory quantity: {self.inventory_value()}")
            print("----------------------------")
            print("Inventory loaded successfully.")
            print("----------------------------")
        except FileNotFoundError:
            print(f"File {file_path} not found.")
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in {file_path}")
        except KeyError as e:
            print(f'Error: Missing required key "{e}" in JSON data.')

        """
        print("Inventory loaded successfully.")
        print(f"Total products: {len(self.products)}")
        print(f"Total inventory value: {self.get_total_inventory_value():.2f} €")
        """
