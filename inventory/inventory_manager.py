from inventory.product import Product
class InventoryManager:
    def __init__(self):
        self.products = {}

    def add_product(self, name, price, quantity):
        if name in self.products:
            raise ValueError(f'Product {name} already exists')
        self.products[name] = Product(name, price, quantity)

    def remove_product(self, name):
        if name not in self.products:
            raise ValueError(f'Product {name} does not exist')
        del self.products[name]

    def update_quantity(self, name, new_quantity):
        if name not in self.products:
            raise ValueError(f'Product {name} does not exist')
        self.products[name].quantity = new_quantity

    def decrease_quantity(self, name, quantity):
        if name not in self.products:
            raise ValueError(f'Product {name} does not exist')
        return self.products[name].decrease_quantity(quantity)
        
    def update_price(self, name, new_price):
        if name not in self.products:
            raise ValueError(f'Product {name} does not exist')
        self.products[name].price = new_price
  

    def retrieve_product_information(self, name):
        if name not in self.products:
            raise ValueError(f'Product {name} does not exist')
        return self.products[name].get_product_info()
    def get_total_inventory_value(self):
        total_value = 0
        for product in self.products.values():
            total_value += product.calculate_total_value()
        return total_value

    
    def inventory_value(self):
        return self.price * self.quantity
    

            
    


    