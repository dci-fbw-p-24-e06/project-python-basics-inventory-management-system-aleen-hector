from .validators import get_valid_input
import colors
class Product:
    def __init__(self,name: str, category: str, price: float, quantity: int):
        self.name: str = name
        self.category: str = category
        self.price: float = price
        self.quantity: float = quantity
    
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
        category: str = input("Category name:")
        price  = get_valid_input("Enter a price: ", "float")
        price = float(price)
        quantity  = get_valid_input("Enter the quantity: ", "int")
        quantity = int(quantity)
        product = Product(name, category, price, quantity)
        self.products.append(product)
        print(f"{product.name} added succesfully")
        return self
    
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
    
    def print_product_info(self):
        """
        Return a dictionary of the object's attributes and values.
        
        This method creates a string (product_info) with each key-value pair formatted with color 
        for the key and left-aligned value minimum width of 12 characters, separated by spaces.
        
        Returns:
            str: A formatted string containing the object's attributes and values.
        """
        #self.__dict__ return a dictionary of the object's attributes and values
        product_info = ' '.join([f"{colors.ANSI_CYAN + key.capitalize() + colors.ANSI_RESET}: {value:<12}" for key, value in self.__dict__.items()])
        return product_info

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
    

