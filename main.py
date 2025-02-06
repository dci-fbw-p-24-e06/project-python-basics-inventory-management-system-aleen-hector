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

def main():
    inventory_manager = InventoryManager()
    inventory_manager.add_product('Product A', 10.99, 100)
    inventory_manager.add_product('Product B', 15.99, 50)
    print(inventory_manager.get_total_inventory_value())  # Output: 549.5
    inventory_manager.update_quantity('Product A', 80)
    print(inventory_manager.get_total_inventory_value())  # Output: 539.5
    inventory_manager.remove_product('Product B')
    print(inventory_manager.get_total_inventory_value())  # Output: 539.5
    inventory_manager.add_product('Product B', 15.99, 50)

    print(inventory_manager.retrieve_product_information('Product A'))  # Output: Product A, 10.99, 100
    print(inventory_manager.retrieve_product_information('Product B')) 
    
    





    

if __name__ == '__main__':
    main()

