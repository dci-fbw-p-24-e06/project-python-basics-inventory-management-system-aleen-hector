from inventory.product import Product, Electronic, Vegetable, Fruit
from .validators import get_valid_input
import colors

def get_subclasses(cls):
    subclasses = cls.__subclasses__()
    list_subclasses = []
    for subclass in subclasses:
        subclasses.extend(get_subclasses(subclass))
        list_subclasses.append(subclass.__name__)
    return list_subclasses

class ProductManager:

    def check_product_exists(func):
        """
        Decorator to check if a product exists in the inventory.

        If the specified product is not found in the inventory, it prints "Product not found"
        and returns None. Otherwise, it calls the decorated function.

        Parameters:
        func: The function to be decorated.

        Returns:
        inner: The decorated function.
        """
        def inner(self, name, *args, **kwargs):
            product = self.find_product(name)
            if not product:
                print("Product not found")
                return None
            return func(self, name, *args, **kwargs)
        return inner
    
    def add_product(self, name: str):
        """
        Add a product to the inventory.
        
        Parameters:
        product (Product): The Product object to add.
        """
        if self.find_product(name):
            return print("Product already exists")
        all_subclasses = get_subclasses(Product)
        while True:
            category: str = input(f"Category name ({get_subclasses(Product)}) : ")
            if category not in all_subclasses:
                print("Category doesn't exist, try again")
            else:
                break
        price  = get_valid_input("Enter a price: ", "float")
        price = float(price)
        quantity  = get_valid_input("Enter the quantity: ", "int")
        quantity = int(quantity)
        if category == "Electronic":
            brand = input("Enter a brand:")
            warranty_period = get_valid_input("Enter a warranty period (in months): ", "int")
            warranty_period = int(warranty_period)
            product = Electronic(name, category, price, quantity, brand, warranty_period)
        elif category == "Vegetable":
            expiry_date = input("Enter expiry date (format mm/yyyy): ")
            product = Vegetable(name, category, price, quantity, expiry_date)
        elif category == "Fruit":
            season = input("Enter the season: ")
            product = Fruit(name, category, price, quantity, season)
        self.products.append(product)
        print(f"{product.name} added succesfully")
        return self

    def check_product_exists(func):
        """
        Decorator to check if a product exists in the inventory.

        If the specified product is not found in the inventory, it prints "Product not found"
        and returns None. Otherwise, it calls the decorated function.

        Parameters:
        func: The function to be decorated.

        Returns:
        inner: The decorated function.
        """
        def inner(self, name, *args, **kwargs):
            product = self.find_product(name)
            if not product:
                print("Product not found")
                return None
            return func(self, name, *args, **kwargs)
        return inner
    
    
    @check_product_exists
    def delete_product(self, name):
        """
        Delete a product from the inventory by name.
        
        Returns:
        list: The updated list of products, or None if the product was not found.
        """
        product = self.find_product(name)
        print(f"Product {product.name} found and deleted from inventory")
        self.products.remove(product)
        return self

    def get_product_info(self, name: str):
        '''
        Print information of a product.
        
        Parameters:
        name (str): The name of the product to get information for.
        '''
        if not self.products:
            print("Inventory is empty")
            return None
        product = self.find_product(name)
        if not product:
            print("Product not found")
            return None
        return product.print_product_info()
    def to_dict(self):
        '''
        convert ANY class object into a dict
        '''
        return {key: value for key, value in self.__dict__.items()}
    
    def update_price(self,name: str, price: float):
        '''
        update the price
        '''
        if not self.products:
            print("Inventory is empty")
            return None
        product = self.find_product(name)
        if not product:
            print("Product not found")
            return None
        product.price = price
        print(f"price of {name} updated to {product.price}")
        return self
    
    def update_quantity(self,name:str, quantity:int):
        '''
        update quantity
        '''
        if not self.products:
            print("Inventory is empty")
            return None
        product = self.find_product(name)
        if not product:
            print("Product not found")
            return None
        product.quantity = quantity
        print(f"Quantity of {name} updated to {product.quantity}")
        return self
    #@check_product_exists
    def total_product_value(self, name):
        '''
        get the total value of a product multiplying the price per quantity
        '''
        product = self.find_product(name)
        if not product:
            print("Product not found")
            return None
        total_value: float = float(product.price) * int(product.quantity)
        return print(f"The total value of {product.name} is: {total_value} euros")