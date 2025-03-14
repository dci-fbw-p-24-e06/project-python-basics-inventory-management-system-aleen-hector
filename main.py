from inventory.inventory_manager import InventoryManager


def main():
    """Main function to run the inventory management system"""
    inventory_manager = InventoryManager()

    def total_value():
        if inventory_manager.get_total_inventory_value() == 0:
            print("The inventory is empty!")
            return
        print(
            f"The total inventory value is {inventory_manager.get_total_inventory_value():.2f} €"
        )

    def remaining_quantity(product_name):
        try:
            print(
                f"Remaining quantity of {product_name}: {inventory_manager.decrease_quantity(product_name, 1)}"
            )
        except ValueError as e:
            print(e)

    def inventory_info(product_name):
        if product_name not in inventory_manager.products:
            print(f"{product_name} does not exist in the inventory")
            return
        product = inventory_manager.products[product_name]
        print(product.get_product_info())
        if product.quantity == 5:
            print(
                f"Remaining quantity {product.name} is low on stock!. Current stock: {product.quantity}"
            )
        elif product.quantity == 0:
            print(f"The {product.name} is out of stock!")

    # Test cases:

    print("\nInitial Inventory:")
    total_value()

    inventory_manager.add_product("Product A", 10.99, 100)
    inventory_manager.add_product("Product B", 15.99, 50)

    total_value()

    inventory_manager.update_quantity("Product A", 80)
    inventory_manager.update_quantity("Product B", 60)
    total_value()

    inventory_manager.remove_product("Product B")
    total_value()
    inventory_manager.add_product("Product B", 18, 70)

    total_value()

    print(inventory_manager.retrieve_product_information("Product A"))
    print(inventory_manager.retrieve_product_information("Product B"))

    inventory_manager.add_product("Product C", 800, 10)
    inventory_manager.update_price("Product C", 500)
    print(inventory_manager.retrieve_product_information("Product A"))

    remaining_quantity("Product C")

    inventory_manager.update_quantity("Product C", 150)
    print(inventory_manager.retrieve_product_information("Product C"))
    inventory_manager.update_price("Product C", 750)
    print(inventory_manager.retrieve_product_information("Product C"))

    inventory_manager.decrease_quantity("Product C", 190)
    print(inventory_manager.retrieve_product_information("Product C"))

    inventory_info("Product C")
    print("\nInventory Value:")
    total_value()


if __name__ == "__main__":
    main()

# Output:
"""
Initial Inventory:
The inventory is empty!
The total inventory value is 1898.50 €
The total inventory value is 1838.60 €
The total inventory value is 879.20 €
The total inventory value is 2139.20 €
Product: Product A, Price: 10.99 €, Quantity: 80
Product: Product B, Price: 18 €, Quantity: 70
Product: Product A, Price: 10.99 €, Quantity: 80
Remaining quantity of Product C: 9
Product: Product C, Price: 500 €, Quantity: 150
Product: Product C, Price: 750 €, Quantity: 150
Cannot decrease quantity beyond stock for product Product C
Product: Product C, Price: 750 €, Quantity: 0
Product: Product C, Price: 750 €, Quantity: 0
The Product C is out of stock!

Inventory Value:
The total inventory value is 2139.20 €"""
