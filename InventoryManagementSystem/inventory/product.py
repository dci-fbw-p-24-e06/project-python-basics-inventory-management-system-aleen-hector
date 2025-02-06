from .validators import get_valid_input
from abc import abstractmethod
import colors
class Product:
    def __init__(self,name: str, category: str, price: float, quantity: int):
        """
        Initialize a Product instance.

        Parameters:
        name (str): The name of the product.
        category (str): The category of the product.
        price (float): The price of the product.
        quantity (int): The quantity of the product in stock.
        """
        self.name: str = name
        self.category: str = category
        self.price: float = price
        self.quantity: int = quantity  

    @classmethod
    def add_product(cls, *args):
        """
        Add a product to the inventory by asking for user input.

        Returns:
        dict: A dictionary containing the product's attributes.
        """
        name = input("Enter product name: ")
        price = get_valid_input("Enter a price: ", "float")
        price = float(price)
        quantity = get_valid_input("Enter the quantity: ", "int")
        quantity = int(quantity)
        return {'Name': name, 'cls': cls.__name__, 'price':price, 'quantity': quantity}
    
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

    def to_dict(self):
        """
        Convert the product's attributes to a dictionary.

        Returns:
        dict: A dictionary containing the product's attributes.
        """
        return {
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'quantity': self.quantity
        }
    
class Vegetable(Product):
    def __init__(self, name, category, price, quantity, expiry_date: str):
        """
        Initialize a Vegetable instance.

        Parameters:
        name (str): The name of the vegetable.
        category (str): The category of the vegetable.
        price (float): The price of the vegetable.
        quantity (int): The quantity of the vegetable in stock.
        expiry_date (str): The expiry date of the vegetable (format mm/yyyy).
        """
        super().__init__(name, category, price, quantity)
        self.expiry_date = expiry_date

    @classmethod
    def add_product(cls, *args, **kwargs):
        """
        Add a vegetable to the inventory by asking for user input.

        Returns:
        Vegetable: The created Vegetable object.
        """
        base_product = super().add_product(cls)
        expiry_date = input("Enter expiry date (format mm/yyyy): ")
        return cls(base_product["Name"], base_product["cls"], base_product["price"], base_product["quantity"], expiry_date)

    def to_dict(self):
        """
        Convert the vegetable's attributes to a dictionary.

        Returns:
        dict: A dictionary containing the vegetable's attributes.
        """
        data = super().to_dict()
        data.update({'expiry_date': self.expiry_date})
        return data

class Fruit(Product):
    def __init__(self, name, category, price, quantity, season):
        """
        Initialize a Fruit instance.

        Parameters:
        name (str): The name of the fruit.
        category (str): The category of the fruit.
        price (float): The price of the fruit.
        quantity (int): The quantity of the fruit in stock.
        season (str): The season when the fruit is available.
        """
        super().__init__(name, category, price, quantity)
        self.season = season

    @classmethod
    def add_product(cls, *args, **kwargs):
        """
        Add a fruit to the inventory by asking for user input.

        Returns:
        Fruit: The created Fruit object.
        """
        base_product = super().add_product(cls)
        season = input("Enter the season: ")
        return cls(base_product["Name"], base_product["cls"], base_product["price"], base_product["quantity"], season)

    def to_dict(self):
        """
        Convert the fruit's attributes to a dictionary.

        Returns:
        dict: A dictionary containing the fruit's attributes.
        """
        data = super().to_dict()
        data.update({'season': self.season})
        return data

class Electronic(Product):
    def __init__(self, name, category, price, quantity, brand: str, warranty_period: int):
        """
        Initialize an Electronic instance.

        Parameters:
        name (str): The name of the electronic product.
        category (str): The category of the electronic product.
        price (float): The price of the electronic product.
        quantity (int): The quantity of the electronic product in stock.
        brand (str): The brand of the electronic product.
        warranty_period (int): The warranty period of the electronic product (in months).
        """
        super().__init__(name, category, price, quantity)
        self.brand = brand
        self.warranty_period = warranty_period

    @classmethod
    def add_product(cls, *args, **kwargs):
        """
        Add an electronic product to the inventory by asking for user input.

        Returns:
        Electronic: The created Electronic object.
        """
        base_product = super().add_product(cls)
        brand = input("Enter a brand: ")
        warranty_period = get_valid_input("Enter a warranty period (in months): ", "int")
        warranty_period = int(warranty_period)
        return cls(base_product["Name"], base_product["cls"], base_product["price"], base_product["quantity"], brand, warranty_period)
    
    def to_dict(self):
        """
        Convert the electronic product's attributes to a dictionary.

        Returns:
        dict: A dictionary containing the electronic product's attributes.
        """
        data = super().to_dict()
        data.update({'brand': self.brand, 'warranty_period': self.warranty_period})
        return data

    

