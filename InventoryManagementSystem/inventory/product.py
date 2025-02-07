from .validators import get_valid_input, validate_expiry_date, validate_season
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
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity  

    @staticmethod
    def get_user_input():
        """
        Prompt the user to input product details including name, price, and quantity.
        
        Returns:
            dict: A dictionary containing the product name, price, and quantity.
                  {
                    "name": str,
                    "price": float,
                    "quantity": int
                  }
        """
        name = input("Enter product name: ")
        price = float(get_valid_input("Enter a price: ", "float"))
        quantity = int(get_valid_input("Enter the quantity: ", "int"))
        return {"name": name, "price":price, "quantity": quantity}
    
    @classmethod
    def add_product(cls, *args, **kwargs):
        """
        Add a product to the inventory by asking for user input.

        Returns:
        dict: A dictionary containing the product's attributes.
        """
        name = kwargs["name"]
        price = kwargs["price"]
        quantity = kwargs["quantity"]
        return {'name': name, 'cls': cls.__name__, 'price':price, 'quantity': quantity}  

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

    @staticmethod
    def get_user_input():
        """
        Get user input for creating a Vegetable instance.

        This method prompts the user for the product name, price, quantity, and expiry_date.
        It validates the input and combines it into a dictionary.

        Returns:
        dict: A dictionary containing the user's input for the vegetable's attributes.
        """
        base_input = Product.get_user_input()
        expiry_date = validate_expiry_date()

        # Combine inputs
        base_input["expiry_date"] = expiry_date
        
        return base_input
    @classmethod
    def add_product(cls, *args, **kwargs):
        """
        Add a vegetable product to the inventory.

        This method extracts the necessary information from the provided arguments
        and creates an instance of the Vegetable class.

        Parameters:
        name (str): The name of the vegetable.
        price (float): The price of the vegetable.
        quantity (int): The quantity of the vegetable in stock.
        expiry_date (str): The expiry date of the vegetable (format mm/yyyy).

        Returns:
        Vegetable: The created Vegetable object.
        """
        # Extract base product and additional properties
        name = kwargs["name"]
        category = cls.__name__
        price = kwargs["price"]
        quantity = kwargs["quantity"]
        expiry_date = kwargs["expiry_date"]

        return cls(name, category, price, quantity, expiry_date)

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

    @staticmethod
    def get_user_input():
        """
        Get user input for creating a Fruit instance.

        This method prompts the user for the product name, price, quantity, and season.
        It validates the input and combines it into a dictionary.

        Returns:
        dict: A dictionary containing the user's input for the fruit's attributes.
        """
        base_input = Product.get_user_input()
        season = validate_season()

        # Combine inputs
        base_input["season"] = season
        
        return base_input
    
    @classmethod
    def add_product(cls, *args, **kwargs):
        """
        Add a fruit product to the inventory.

        This method extracts the necessary information from the provided arguments
        and creates an instance of the Vegetable class.

        Parameters:
        name (str): The name of the vegetable.
        price (float): The price of the vegetable.
        quantity (int): The quantity of the vegetable in stock.
        season (str): The season of the Fruit.

        Returns:
        Fruit: The created Vegetable object.
        """
        # Extract base product and additional properties
        name = kwargs["name"]
        category = cls.__name__
        price = kwargs["price"]
        quantity = kwargs["quantity"]
        season = kwargs["season"]

        return cls(name, category, price, quantity, season)

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
    
    @staticmethod
    def get_user_input():
        """
        Get user input for creating a Electronic instance.

        This method prompts the user for the product name, price, quantity, brand and warranty_period.
        It validates the input and combines it into a dictionary.

        Returns:
        dict: A dictionary containing the user's input for the electronic's attributes.
        """
        base_input = Product.get_user_input()
        brand = input("Enter a brand: ")
        warranty_period = int(get_valid_input("Enter a warranty period (in months): ", "int"))
        # Combine inputs
        base_input["brand"] = brand
        base_input["warranty_period"] = warranty_period
        
        return base_input
    @classmethod
    def add_product(cls, *args, **kwargs):
        """
        Add an electronic product to the inventory.

        This method extracts the necessary information from the provided arguments
        and creates an instance of the Electronic class.

        Parameters:
        name (str): The name of the electronic product.
        price (float): The price of the electronic product.
        quantity (int): The quantity of the electronic product in stock.
        brand (str): The brand of the electronic product.
        warranty_period (int): The warranty period of the electronic product (in months).

        Returns:
        Electronic: The created Electronic object.
        """
        # Extract base product and additional properties
        name = kwargs["name"]
        category = cls.__name__
        price = kwargs["price"]
        quantity = kwargs["quantity"]
        brand = kwargs["brand"]
        warranty_period = kwargs["warranty_period"]

        return cls(name, category, price, quantity, brand, warranty_period)
    
    def to_dict(self):
        """
        Convert the electronic product's attributes to a dictionary.

        Returns:
        dict: A dictionary containing the electronic product's attributes.
        """
        data = super().to_dict()
        data.update({'brand': self.brand, 'warranty_period': self.warranty_period})
        return data

    

