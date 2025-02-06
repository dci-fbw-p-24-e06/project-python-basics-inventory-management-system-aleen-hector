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
            raise ValueError('Not enough stock')
        self.quantity -= quantity
        return self.quantity
    
    def increase_quantity(self, quantity):
        self.quantity += quantity
        return self.quantity
    
    def calculate_total_value(self):
        return self.price * self.quantity
    
    def __str__(self):
        return f'Product: {self.name}, Price: ${self.price}, Quantity: {self.quantity}'
    
    def get_product_info(self):
        return {
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
        }
    
    