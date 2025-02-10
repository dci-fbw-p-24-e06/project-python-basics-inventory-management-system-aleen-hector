from InventoryManagementSystem.inventory.product import Vegetable, Fruit, Electronic
from inventory.inventory_manager import InventoryManager
from inventory.products_manager import ProductManager
   
if __name__ == "__main__":
   # Initialize ProductManager
   product_manager = ProductManager()
   inventory = InventoryManager()

   #show inventory is empty
   print("SHOW INVENTORY")
   inventory.show_inventory()
   
   #ADDING DATA 

   # Vegetables
   vegetable_data = [
      {"name": "Carrot", "price": 1.50, "quantity": 50, "expiry_date": "12/2025"},
      {"name": "Broccoli", "price": 2.00, "quantity": 30, "expiry_date": "01/2026"},
      {"name": "Spinach", "price": 1.25, "quantity": 40, "expiry_date": "11/2025"},
      {"name": "Potato", "price": 0.75, "quantity": 100, "expiry_date": "09/2025"}
   ]
   for data in vegetable_data:
      new_vegetable = Vegetable.add_product(**data)
      inventory.add_product(new_vegetable)

   # Fruits
   fruit_data = [
      {"name": "Apple", "price": 0.50, "quantity": 100, "season": "Autumn"},
      {"name": "Banana", "price": 0.30, "quantity": 120, "season": "All year"},
      {"name": "Cherry", "price": 3.00, "quantity": 25, "season": "Summer"},
      {"name": "Orange", "price": 0.60, "quantity": 80, "season": "Winter"}
   ]
   for data in fruit_data:
      new_fruit = Fruit.add_product(**data)
      inventory.add_product(new_fruit)
  
   # Electronics
   electronic_data = [
      {"name": "Laptop", "price": 999.99, "quantity": 10, "brand": "TechBrand", "warranty_period": 24},
      {"name": "Smartphone", "price": 699.99, "quantity": 20, "brand": "PhoneBrand", "warranty_period": 12},
      {"name": "Tablet", "price": 399.99, "quantity": 15, "brand": "TabBrand", "warranty_period": 18},
      {"name": "Headphones", "price": 199.99, "quantity": 30, "brand": "SoundBrand", "warranty_period": 12},
      {"name": "Smartwatch", "price": 299.99, "quantity": 25, "brand": "WatchBrand", "warranty_period": 24}
   ]
   for data in electronic_data:
      new_electronic = Electronic.add_product(**data)
      inventory.add_product(new_electronic)

   #Functions testing after adding data
   print("SHOW INVENTORY:")
   inventory.show_inventory()
   #
   print("INVENTORY TOTAL VALUE:")
   inventory.total_inventory_value()
   
   #ProductManager TESTING

   print("DELETE PRODUCT CARROT")
   ProductManager.delete_product(inventory,"Carrott")
   ProductManager.delete_product(inventory,"Carrot")
   print("INVENTORY TOAL VALUE AFTER DELETING CARROT:")
   inventory.total_inventory_value()
   #delete and adding
   orange = Fruit.add_product(name="Orange", price=0.60, quantity=80, season="Winter")
   inventory.add_product(orange)
   ProductManager.delete_product(inventory,"Orange")
   orange = Fruit.add_product(name="Orange", price=0.60, quantity=80, season="Winter")
   inventory.add_product(orange)
   #updating data from a product
   print("UPDATING PRICE AND QUANTITY ")
   print(ProductManager.get_product_info(inventory, "Orange"))
   ProductManager.total_product_value(inventory, "Orange")
   ProductManager.update_price(inventory, "Orange", 0.75)
   ProductManager.update_quantity(inventory, "Orange", 10)
   print(ProductManager.get_product_info(inventory, "Orange"))
   ProductManager.total_product_value(inventory, "Orange")

   #InventoryManager TESTING

   print("SHOWING PRODUCTS FROM CATEGORY")
   print(f"Products from category Fruit:")
   inventory.product_summary_category("Fruit")
   print(f"Products from category Vegetable:")
   inventory.product_summary_category("Vegetable")
   print(f"Products from category Electronic:")
   inventory.product_summary_category("Electronic")
   print(f"Products from category Fruitss:")
   inventory.product_summary_category("Fruitss")
   #sorting inventory
   print("INVENTOY SORTING")
   print("SORTING BY NAME")
   inventory.sort_by_attr("name")
   inventory.show_inventory()
   
   print("SORTING BY CATEGORY")
   inventory.sort_by_attr("category")
   inventory.show_inventory()

   print("SORTING BY PRICE")
   inventory.sort_by_attr("price")
   inventory.show_inventory()

   print("SORTING BY QUANTITY")
   inventory.sort_by_attr("quantity")
   inventory.show_inventory()
   #show graphs
   inventory.show_graph_product_value()
   inventory.show_pie_graph_products()
   


