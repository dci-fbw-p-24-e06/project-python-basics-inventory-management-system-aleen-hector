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

    
    def get_product_info(self):
        '''
        print information of a product
        '''
        product_info = (
            f"Name: {self.name}, "
            f"Category:{self.category}, "
            f"Price: {self.price}, "
            f"Quantity: {self.quantity}"
        )
        return product_info
   
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
    @check_product_exists
    def total_product_value(self):
        '''
        get the total value of a product multiplying the price per quantity
        '''
        total_value: float = self.price * self.quantity
        return f"The total value of {self.name} is: {total_value} euros"
    

