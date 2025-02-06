
from inventory.inventory_manager import InventoryManager


def main():
    inventory_manager = InventoryManager()
    
    def inventory_info(product):
        print(product.get_product_info())
        if product.quantity == 5:
            print(f'Remaining quantity {product.name} is low on stock!, current stock: {product.quantity}')
        elif product.quantity == 0:
            print(f'The {product.name} is out of stock!')
            
        

    def total_value():
         if inventory_manager.get_total_inventory_value() == 0:
             print('The inventory is empty!')
             return
         print(f'The total inventory value is {inventory_manager.get_total_inventory_value():.2f} €') 

    def remaining_quantity(product_name):
        try:
            print(f'Remaining quantity of {product_name}: {inventory_manager.decrease_quantity(product_name, 1)}')
        except ValueError as e:
            print(e)

# Test cases:

    print('\nInitial Inventory:')
    total_value()

    inventory_manager.add_product('Product A', 10.99, 100)
    inventory_manager.add_product('Product B', 15.99, 50)

    inventory_info(inventory_manager.products['Product A'])   
    inventory_info(inventory_manager.products['Product B'])  
    total_value()
    
    inventory_manager.update_quantity('Product A', 80)
    inventory_manager.update_quantity('Product B', 60)
    total_value()
    

    inventory_manager.remove_product('Product B')
    total_value()
    inventory_manager.add_product('Product B', 18, 70)

    total_value()


    print(inventory_manager.retrieve_product_information('Product A'))  
    print(inventory_manager.retrieve_product_information('Product B')) 
    
    
    inventory_manager.add_product('Product C', 800, 10)
    inventory_info(inventory_manager.products['Product C'])  
    print(inventory_manager.retrieve_product_information('Product C'))  
    
    
    remaining_quantity('Product C')
 

    inventory_manager.update_quantity('Product C', 150)
    print(inventory_manager.retrieve_product_information('Product C'))  
    inventory_manager.update_price('Product C', 750)
    print(inventory_manager.retrieve_product_information('Product C'))  

    inventory_manager.decrease_quantity('Product C', 190)
    print(inventory_manager.retrieve_product_information('Product C'))



if __name__ == "__main__":
    main()

