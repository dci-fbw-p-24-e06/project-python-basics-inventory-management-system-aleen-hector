import PySimpleGUI as sg
from datetime import datetime
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
        Prompt the user to input product details including name, price, and quantity using a GUI.
        
        Returns:
            dict: A dictionary containing the product name, price, and quantity.
                {
                    "name": str,
                    "price": float,
                    "quantity": int
                }
        """
        layout = [
            [sg.Text("Enter product name:"), sg.InputText(key="name")],
            [sg.Text("Enter price:"), sg.InputText(key="price")],
            [sg.Text("Enter quantity:"), sg.InputText(key="quantity")],
            [sg.Submit(), sg.Cancel()]
        ]

        window = sg.Window("Product Input", layout)

        while True:
            event, values = window.read()
            if event == "Submit":
                try:
                    name = values["name"]
                    price = float(values["price"])
                    quantity = int(values["quantity"])
                    window.close()
                    return {"name": name, "price": price, "quantity": quantity}
                except ValueError:
                    sg.popup_error("Please enter valid data for price and quantity.")
            elif event in (sg.WINDOW_CLOSED, "Cancel"):
                window.close()
                return None
    
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
        product_info = ' '.join([f"{key.capitalize()}: {value:12}" for key, value in self.__dict__.items()])
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
        Get user input for creating a Vegetable instance using a GUI.

        This method prompts the user for the product name, price, quantity, and expiry_date.
        It validates the input and combines it into a dictionary.

        Returns:
        dict: A dictionary containing the user's input for the vegetable's attributes.
        """
        # Base input using the Product's get_user_input method
        base_input = Product.get_user_input()
        
        layout = [
            [sg.Text("Enter expiry date (dd/mm/yyyy):"), sg.InputText(key="expiry_date")],
            [sg.Submit(), sg.Cancel()]
        ]

        window = sg.Window("Vegetable Input", layout)

        while True:
            event, values = window.read()
            if event == "Submit":
                try:
                    expiry_date_str = values["expiry_date"]
                    # Validate date format
                    expiry_date = datetime.strptime(expiry_date_str, "%d/%m/%Y")
                    # Combine inputs
                    base_input["expiry_date"] = expiry_date_str
                    window.close()
                    return base_input
                except ValueError:
                    sg.popup_error("Please enter a valid date in the format dd/mm/yyyy.")
            elif event in (sg.WINDOW_CLOSED, "Cancel"):
                window.close()
                return None
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
        Get user input for creating a Fruit instance using a GUI.

        This method prompts the user for the product name, price, quantity, and season.
        It validates the input and combines it into a dictionary.

        Returns:
        dict: A dictionary containing the user's input for the fruit's attributes.
        """
        # Base input using the Product's get_user_input method
        base_input = Product.get_user_input()
        
        layout = [
            [sg.Text("Enter season:"), sg.InputText(key="season")],
            [sg.Submit(), sg.Cancel()]
        ]

        window = sg.Window("Fruit Input", layout)

        while True:
            event, values = window.read()
            if event == "Submit":
                season = values["season"]
                # Combine inputs
                base_input["season"] = season
                window.close()
                return base_input
            elif event in (sg.WINDOW_CLOSED, "Cancel"):
                window.close()
                return None
    
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
        Get user input for creating an Electronic instance using a GUI.

        This method prompts the user for the product name, price, quantity, brand, and warranty_period.
        It validates the input and combines it into a dictionary.

        Returns:
        dict: A dictionary containing the user's input for the electronic's attributes.
        """
        # Base input using the Product's get_user_input method
        base_input = Product.get_user_input()
        
        layout = [
            [sg.Text("Enter brand:"), sg.InputText(key="brand")],
            [sg.Text("Enter warranty period (in months):"), sg.InputText(key="warranty_period")],
            [sg.Submit(), sg.Cancel()]
        ]

        window = sg.Window("Electronic Input", layout)

        while True:
            event, values = window.read()
            if event == "Submit":
                try:
                    brand = values["brand"]
                    warranty_period = int(values["warranty_period"])
                    # Combine inputs
                    base_input["brand"] = brand
                    base_input["warranty_period"] = warranty_period
                    window.close()
                    return base_input
                except ValueError:
                    sg.popup_error("Please enter valid data for warranty period.")
            elif event in (sg.WINDOW_CLOSED, "Cancel"):
                window.close()
                return None
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

    

