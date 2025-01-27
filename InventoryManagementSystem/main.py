from inventory.inventory_manager import InventoryManager
from inventory.product import Product
from inventory.validators import get_valid_input
def show_menu():
    """ 
    Display the menu options to the user. 

    Prints a list of task options that the user can choose from. 
    """
    menu = ( 
            "==================================================\n" 
            "===        INVENTORY MANAGING SYSTEM        ===\n"
            "==================================================\n" 
            " Please choose one of the following tasks:\n"
            " 1.    Add product \n" 
            " 2.    Remove product \n" 
            " 3.    See product information \n"
            " 4.    See inventory \n"
            " 5.    Total Product Value \n"
            " 6.    See products by category \n"
            " 18.    Save inventory to JSON \n"
            " 19.    Load inventory from JSON \n"
            " 20.   Exit\n"
            "==================================================\n"
    ) 
    print(menu)

def main():
    """ 
    Main function to display the menu and handle user input. 
    
    Continuously displays a menu to the user and processes their input to execute 
    the corresponding tasks. 
    
    Validates that the user input is a number and calls the appropriate functions based on the chosen task number. 
    The loop continues until the user chooses to exit. 
    """
    inventory = InventoryManager()
    while True:
        show_menu()
        # Validate if the input is an integer 
        chosen_number = get_valid_input("What you want to do? ", "int")
        
        # Proceed with the task selection
        chosen_number = int(chosen_number) 

        if chosen_number == 1:
            name: str = input("Name of the product: ")
            print(Product.add_product(inventory, name))
            keepOn()
        elif chosen_number == 2:
            name: str = input("Name of the product: ")
            Product.delete_product(inventory, name)
            keepOn()
        elif chosen_number == 3:
            name: str = input("Name of the product: ")
            product_info = Product.get_product_info(inventory, name)
            if product_info:
                print(product_info)
            keepOn()    
        elif chosen_number == 4:
            print("Inventory list:")
            print("*"*20)
            inventory.show_inventory()
            keepOn()
        elif chosen_number == 5:
            name: str = input("Name of the product:")
            print(Product.total_product_value(inventory, name))
            keepOn()
        elif chosen_number == 5:
            category: str = input("For wich category you want to see the products:")
            InventoryManager.product_summary_category(inventory, category)
            keepOn()
        elif chosen_number == 18:
            filename = input("Enter the filename to save the inventory (e.g., inventory.json): ")
            inventory.save_to_json(filename)
            keepOn()
        elif chosen_number == 19:
            filename = input("Enter the filename to load the inventory (e.g., inventory.json): ")
            inventory.load_from_json(filename)
            keepOn()
        elif chosen_number == 20:
            print("See you next time")
            break
        else:
            print("this option doesn't exist, try again")

def keepOn(): 
    """ 
    Pause the program to wait for user input to continue. 
    Prompts the user to press Enter to continue. 
    """ 
    input("\nPress Enter to continue...")


#run the programm
main()