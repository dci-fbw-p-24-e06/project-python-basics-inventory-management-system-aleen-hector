from .validators import get_valid_input
class Product:
    def __init__(self,name: str, category: str, price: float, quantity: int):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
    '''
    #decorator
    def check_product_exists(func):
        def inner(self, name, *args, **kwargs):
            product = find_product(name)
            if not product:
                print("Product not found")
                return None
            return func(self, name, *args, **kwargs)
        return inner
    '''
    @staticmethod
    def add_product(inventory, name: str):
        """
        Add a product to the inventory.
        
        Parameters:
        product (Product): The Product object to add.
        """
        if inventory.find_product(name):
            return f"Product already exists"
        category: str = input("Category name:")
        price = get_valid_input("Enter a price: ", "float")
        price = float(price)
        quantity = get_valid_input("Enter the quantity: ", "int")
        quantity = int(quantity)
        product = Product(name, category, price, quantity)
        inventory.products.append(product)
        print(f"{product.name} added succesfully")
        return inventory
    @staticmethod
    def delete_product(inventory, name):
        """
        Delete a product from the inventory by name.
        
        Returns:
        list: The updated list of products, or None if the product was not found.
        """
        product = inventory.find_product(name)
        if not product:
            print("Product not found")
            return None
        print(f"Product {product.name} found and deleted from inventory")
        inventory.products.remove(product)
        return inventory
    
    def print_product_info(self):
        '''
        Print information of a product.
        '''
        product_info = (
            f"Name: {self.name}, "
            f"Category: {self.category}, "
            f"Price: {self.price}, "
            f"Quantity: {self.quantity}"
        )
        return product_info
   
    @staticmethod
    def get_product_info(inventory, name: str):
        '''
        Print information of a product.
        
        Parameters:
        name (str): The name of the product to get information for.
        '''
        if not inventory.products:
            print("Inventory is empty")
            return None
        product = inventory.find_product(name)
        if not product:
            print("Product not found")
            return None
        return product.print_product_info()
    
    def to_dict(self):
        '''
        convert a product class object into a dict
        '''
        return {
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "quantity": self.quantity
        }
    
    def update_price(self,price: float):
        '''
        update the price
        '''
        self.price = price
        return "price of {self.name} updated to {self.price}"
    
    def update_quantity(self,quantity: int):
        '''
        update quantity
        '''
        self.quantity = quantity
        return f"Quantity of {self.name} updated to {self.quantity}"
    #@check_product_exists
    def total_product_value(inventory, name):
        '''
        get the total value of a product multiplying the price per quantity
        '''
        product = inventory.find_product(name)
        if not product:
            print("Product not found")
            return None
        total_value: float = product.price * product.quantity
        return f"The total value of {product.name} is: {total_value} euros"
    

