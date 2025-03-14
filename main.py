import os
from inventory.inventory_manager import InventoryManager

def main():
    """Main function to run the inventory management system."""
    
    # Ensure JSON file exists before loading
    filename = "inventory.json"
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            file.write('{"products": []}')  # Initialize with empty products
    
    inventory = InventoryManager(filename)  # ✅ Loads inventory

    while True:
        print("\n📦 Inventory Management System")
        print("1️⃣ Add Product")
        print("2️⃣ Remove Product")
        print("3️⃣ Update Product Quantity")
        print("4️⃣ Search Product")
        print("5️⃣ Display Inventory")
        print("6️⃣ Exit")
        
        choice = input("🔹 Choose an option (1-6): ")
        
        if choice == "1":
            name = input("Enter product name: ")
            category = input("Enter category: ")
            price = float(input("Enter price (€): "))
            quantity = int(input("Enter quantity: "))
            inventory.add_product(name, category, price, quantity)
        
        elif choice == "2":
            name = input("Enter product name to remove: ")
            try:
                inventory.remove_product(name)
                print(f"✅ Product '{name}' removed.")
            except ValueError as e:
                print(f"❌ {e}")
        
        elif choice == "3":
            name = input("Enter product name: ")
            quantity = int(input("Enter new quantity: "))
            try:
                inventory.update_quantity(name, quantity)
                print(f"✅ Updated quantity for '{name}'.")
            except ValueError as e:
                print(f"❌ {e}")
        
        elif choice == "4":
            name = input("Enter product name to search: ")
            result = inventory.search_product(name)
            if result:
                for product in result:
                    print(product.get_product_info())
            else:
                print(f"❌ Product '{name}' not found.")

        elif choice == "5":
            inventory.display_inventory()  # ✅ Now correctly displays loaded inventory
        
        elif choice == "6":
            print("📦 Exiting... Inventory saved.")
            inventory.save_inventory()  # ✅ Ensure all changes are saved before exit
            break
        
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()


