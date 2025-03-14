import json
from inventory.product import Product


class InventoryManager:
    """Manages the inventory of products"""
    def __init__(self):
        """Initialize an empty inventory"""
        self.products = {}

    def add_product(self, name: str, category: str, price: float, quantity: int) -> None:
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
            raise ValueError(f'Product {name} already exists')
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
            raise ValueError(f'Product {name} does not exist')
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
            raise ValueError(f'Product {name} does not exist.')
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
            raise ValueError(f'Product {name} does not exist.')
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
            return f'Product {product_name} does not exist in the inventory'
        
        product = self.products[product_name]
        info = product.get_inventory_info()

        if product.quantity == 5:
            return (
                f'{info}\n⚠️ Warning: {product_name} is low on stock!'
                f'Only {product.quantity} left.'
            )
        if product.quantity == 0:
            return f'{info}\n❌ {product_name} is out of stock!'

    def get_total_inventory_value(self):
        total_value = 0
        for product in self.products.values():
            total_value += product.calculate_total_value()
        return total_value

    def get_product(self, product_name):
        return self.products.get(product_name)

    def inventory_value(self):
        return self.price * self.quantity
