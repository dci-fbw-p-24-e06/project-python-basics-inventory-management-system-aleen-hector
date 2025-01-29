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
    
    def is_inventory_empty(func):
        def inner(self, *args, **kwargs):
            if not self.products:
                print("Inventory is empty")
                return None
            return func(self, *args, **kwargs)
        return inner
    """#decorator
    def check_product_exists(func):
        def inner(self, name, *args, **kwargs):
            product = func.find_product(name)
            if not product:
                print("Product not found")
                return None
            return func(self, name, *args, **kwargs)
        return inner
     """
    @is_inventory_empty
    def show_inventory(self):
        '''
        print the inventory with product information
        '''
        for product in self.products:
            print(product.print_product_info())
    @is_inventory_empty
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