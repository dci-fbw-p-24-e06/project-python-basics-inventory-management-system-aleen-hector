from inventory.inventory_manager import InventoryManager


def main():
    inventory_manager = InventoryManager()
    inventory_manager.load_from_json("inventory_data.json")
    inventory_manager.display_inventory()

    # Adding new products from JSON structure
    inventory_manager.add_product("Smartphone", "Electronics", 999, 3)
    inventory_manager.add_product("Office Chair", "Furniture", 150, 7)

    inventory_manager.display_inventory()


if __name__ == "__main__":
    main()
