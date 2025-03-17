import json
from inventory.inventory_manager import InventoryManager

def main():
    inventory = InventoryManager()  # Load inventory from JSON

    while True:
        print("\n🏬 Inventory Management System")
        print("1️⃣ Add Product")
        print("2️⃣ Remove Product")
        print("3️⃣ Update Product Quantity")
        print("4️⃣ Search Product")
        print("5️⃣ Display Inventory")
        print("6️⃣ Update Product Price")
        print("7️⃣ Show Total Inventory Value")
        print("8️⃣ Show Total Inventory Quantity")
        print("9️⃣ Exit")
        
        choice = input("\n❇️  Choose an option (1-9): ")

        if choice == "1":
            name = input("Enter product name: ").strip()
            category = input("Enter category: ").strip()
            price = float(input("Enter price (€): "))
            quantity = int(input("Enter quantity: "))
            inventory.add_product(name, category, price, quantity)

        elif choice == "2":
            name = input("Enter product name to remove: ").strip()
            inventory.remove_product(name)

        elif choice == "3":
            name = input("Enter product name to update quantity: ").strip()
            new_quantity = int(input("Enter new quantity: "))
            inventory.update_quantity(name, new_quantity)

        elif choice == "4":
            name = input("Enter product name to search: ").strip()
            inventory.search_product(name)

        elif choice == "5":
            inventory.display_inventory()

        elif choice == "6":
            name = input("Enter product name to update price: ").strip()
            new_price = float(input("Enter new price (€): "))
            inventory.update_price(name, new_price)

        elif choice == "7":
            total_value = inventory.get_total_inventory_value()
            print(f"📊 Total Inventory Value: {total_value:.2f}€")

        elif choice == "8":
            total_quantity = inventory.inventory_quantity()
            print(f"📦 Total Inventory Quantity: {total_quantity} items")

        elif choice == "9":
            print("🚪 Exiting... Inventory saved.")
            inventory.save_inventory()  # Save inventory before exiting
            break

        else:
            print("❌ Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()