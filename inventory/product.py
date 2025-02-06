class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        return self.quantity

    def update_price(self, new_price):
        self.price = new_price
        return self.price
    
    def decrease_quantity(self, quantity):
        if self.quantity - quantity < 0:
            raise ValueError(f'Cannot decrease quantity beyond stock for product {self.name}')
        self.quantity -= quantity
        return self.quantity
        
    
    
    def calculate_total_value(self):
        return self.price * self.quantity
    
    
    def get_product_info(self):
        return f'Product: {self.name}, Price: {self.price} €, Quantity: {self.quantity}'
    
