# add product
# add_product(product_name, price, quantity)
# product_name: str, price: float, quantity: int
# remove_product(product_name)
# update quantity(product_name, new_quantity)
# retrieve product information(product_name)
# calculate_total_inventory_value()

# create classes to represent products and inventory
# class Product:

# create inventory manager to handle inventory operations

# implement unit tests
# from unittest import TestCase
# mock external dependencies (e.g., database)

## Project structure
'''
InventoryManagementSystem/
├── inventory/
│   ├── __init__.py
│   ├── product.py
│   └── inventory_manager.py
├── tests/
│   ├── __init__.py
│   └── test_inventory_manager.py
└── main.py
'''

# main.py

from inventory.inventory_manager import InventoryManager
from inventory.product import Product

def main():
    inventory_manager = InventoryManager()

    def inventory_info(product):
        print(product.get_product_info())
        print(f'Remaining quantity of {product.name}: {product.quantity}')
        

    def total_value():
         print(f'\nThe total inventory value is {inventory_manager.get_total_inventory_value():.2f} €')   

    inventory_manager.add_product('Product A', 10.99, 100)
    inventory_manager.add_product('Product B', 15.99, 50)
    inventory_info(inventory_manager.products['Product A'])  # Output: Product A, 10.99, 100  
    inventory_info(inventory_manager.products['Product B'])  # Output: Product B, 15.99, 50
    total_value()
    
    inventory_manager.update_quantity('Product A', 80)
    inventory_manager.update_quantity('Product B', 60)
    total_value()
    

    inventory_manager.remove_product('Product B')
    total_value()
    inventory_manager.add_product('Product B', 18, 70)

    total_value()


    print(inventory_manager.retrieve_product_information('Product A'))  # Output: Product A, 10.99, 100
    print(inventory_manager.retrieve_product_information('Product B')) 
    
    
    inventory_manager.add_product('Product C', 800, 10)
    inventory_info(inventory_manager.products['Product C'])  # Output: Prorint_inventory_info(inv) # Output: Product C, 800, 10
    print(inventory_manager.retrieve_product_information('Product C'))  # Output: Product C, 800, 10
    try:
        remaining_quantity = inventory_manager.decrease_quantity('Product C', 3)
        print(f'Remaining quantity of Product C: {remaining_quantity}')  # Output: Remaining quantity of Product C: 50
    except ValueError as e:
        print(e)    
 

    inventory_manager.update_quantity('Product C', 150)
    print(inventory_manager.retrieve_product_information('Product C'))  # Output: Product C, 750, 50   

    inventory_manager.update_price('Product C', 750)
    print(inventory_manager.retrieve_product_information('Product C'))  # Output: Product C, 750, 0

    inventory_manager.decrease_quantity('Product C', 50)







    

if __name__ == '__main__':
    main()

