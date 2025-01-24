from .product import Product
from .validators import get_valid_input
import json
class InventoryManager:
    def __init__(self,products = None):
        """
        Initialize the InventoryManager with a list of products.
        
        Parameters:
        products (list): A list of Product objects. Defaults to an empty list if not provided.
        """
        if products is None:
            products = []
        self.products = products
    def find_product(self, product_name: str) -> Product:
        """
        Find a product in the inventory by name.
        
        Parameters:
        product_name (str): The name of the product to find.
        
        Returns:
        Product: The Product object if found, None otherwise.
        """
        for product in self.products:
            if product.name == product_name:
                return product
        return None
    
    #decorator
    def check_product_exists(func):
        def inner(self, name, *args, **kwargs):
            product = func.find_product(name)
            if not product:
                print("Product not found")
                return None
            return func(self, name, *args, **kwargs)
        return inner

    def add_product(self):
        """
        Add a product to the inventory.
        
        Parameters:
        product (Product): The Product object to add.
        """
        name: str = input("Name of the product:")
        if self.find_product(name):
            return f"Product already exists"
        category: str = input("Category name:")
        price = get_valid_input("Enter a price: ", "float")
        price = float(price)
        quantity = get_valid_input("Enter the quantity: ", "int")
        quantity = int(quantity)
        product = Product(name, category, price, quantity)
        self.products.append(product)
        return f"{product.name} added succesfully"
    def delete_product(self, name):
        """
        Delete a product from the inventory by name.
        
        Returns:
        list: The updated list of products, or None if the product was not found.
        """
        product = self.find_product(name)
        if not product:
            print("Product not found")
            return None
        else:
            print(f"Product {product.name} found and deleted from inventory")
            self.products.remove(product)
            return self.products
        
    '''
    print the inventory with product information
    '''
    def show_inventory(self):
        if self.products:
            for product in self.products:
                print(product.get_product_info())
        else:
            print("Inventory is empty")
    def product_summary_category(self, category):
        list_products = []
        for product in self.products:
            if product.category == category:
                list_products.append(product.name)
        if not list_products:
            print("This category doesn't exists already or have not products")
        else:
            print(", ".join(list_products))
    
    def save_to_json(self, filename):
        """
        Save the inventory data to a JSON file.
        
        Parameters:
        filename (str): The name of the file to save the inventory data to.
        """
        with open(filename, 'w') as file:
            json.dump([product.to_dict() for product in self.products], file, indent=3)
        print(f"Inventory saved to {filename}")

    def load_from_json(self, filename):
        """
        Load the inventory data from a JSON file.
        
        Parameters:
        filename (str): The name of the file to load the inventory data from.
        """
        try:
            with open(filename, 'r') as file:
                products_data = json.load(file)
                self.products = [Product(**data) for data in products_data]
            print(f"Inventory loaded from {filename}")
        except FileNotFoundError:
            print(f"No such file: {filename}")

'''
# Example usage
water = Product("Water", "Drink", 0.5, 100)
milk = Product("milk", "Drink", 1.1, 20)

inventory_manager = InventoryManager([water, milk])

inventory_manager.add_product(Product("Banane", "Fruit",0.2, 15))
inventory_manager.get_products_info()
inventory_manager.delete_product("Banane")

inventory_manager.get_products_info()
print(water.total_product_value())'''