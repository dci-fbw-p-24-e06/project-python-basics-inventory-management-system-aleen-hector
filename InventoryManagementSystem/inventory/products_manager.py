from inventory.product import Product, Electronic, Vegetable, Fruit

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
    
    def add_product(self):
        """
        Add a product to the inventory by asking for user input.
        
        This method prompts the user to input a category name, checks if the category exists, 
        and then prompts the user for additional product details based on the category.
        
        If the product does not already exist in the inventory, it is added.
        
        Returns:
        self: The inventory instance with the newly added product.
        """
        all_subclasses = get_subclasses(Product)
        while True:
            category: str = input(f"from which category do you want to add a product ({get_subclasses(Product)}) ? ")
            if category not in all_subclasses:
                print("Category doesn't exist, try again")
            else:
                break
        if category == "Electronic":
            data = Electronic.get_user_input()
            product = Electronic.add_product(**data)
        elif category == "Vegetable":
            data = Vegetable.get_user_input()
            product = Vegetable.add_product(**data)
        elif category == "Fruit":
            data = Fruit.get_user_input()
            product = Fruit.add_product(**data)
        if not self.find_product(product.name):
            self.products.append(product)
            print(f"{product.name} added succesfully")
            return product
        else:
            print("Product already exists in the inventory")
            return None

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