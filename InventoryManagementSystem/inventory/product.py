from .validators import get_valid_input
import colors
class Product:
    def __init__(self,name: str, category: str, price: float, quantity: int):
        self.name: str = name
        self.category: str = category
        self.price: float = price
        self.quantity: int = quantity
    
    
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

    
class Vegetable(Product):
    def __init__(self, name, category, price, quantity, expiry_date: str):
        super().__init__(name, category, price, quantity)
        self. expiry_date = expiry_date

class Fruit(Product):
    def __init__(self, name, category, price, quantity, season):
        super().__init__(name, category, price, quantity)
        self.season = season

class Electronic(Product):
    def __init__(self, name, category, price, quantity, brand: str, warranty_period: int):
        super().__init__(name, category, price, quantity)
        self.brand = brand
        self.warranty_period = warranty_period

    

