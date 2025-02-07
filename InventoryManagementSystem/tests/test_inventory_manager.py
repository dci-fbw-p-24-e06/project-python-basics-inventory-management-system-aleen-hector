import InventoryManagementSystem.inventory.inventory_manager
def main():
   inventory = InventoryManager()
   inventory = [
   {
      "name": "Apple",
      "category": "Fruit",
      "price": 0.5,
      "quantity": 20,
      "season": "Fall"
   },
   {
      "name": "Mango",
      "category": "Fruit",
      "price": 1.5,
      "quantity": 8,
      "season": "Summer"
   },
   {
      "name": "Pineapple",
      "category": "Fruit",
      "price": 2.0,
      "quantity": 6,
      "season": "Summer"
   },
   {
      "name": "Carrot",
      "category": "Vegetable",
      "price": 0.4,
      "quantity": 30,
      "expiry_date": "12/06/2024"
   },
   {
      "name": "Cucumber",
      "category": "Vegetable",
      "price": 0.6,
      "quantity": 25,
      "expiry_date": "12/08/2024"
   },
   {
      "name": "Bell Pepper",
      "category": "Vegetable",
      "price": 0.7,
      "quantity": 18,
      "expiry_date": "13/09/2024"
   },
   {
      "name": "Laptop",
      "category": "Electronic",
      "price": 800.0,
      "quantity": 3,
      "brand": "Dell",
      "warranty_period": 24
   },
   {
      "name": "Tablet",
      "category": "Electronic",
      "price": 300.0,
      "quantity": 7,
      "brand": "Apple",
      "warranty_period": 12
   },
   {
      "name": "Smartwatch",
      "category": "Electronic",
      "price": 150.0,
      "quantity": 10,
      "brand": "Fitbit",
      "warranty_period": 12
   }
]
   # Initialize ProductManager
   ProductManager.delete_product(inventory,"Spinach")
   ProductManager.delete_product(inventory,"Smartwatch")
   InventoryManager.show_inventory(inventory)

   if __name__ == "__main__":
    main()