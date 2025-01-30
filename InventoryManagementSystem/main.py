from inventory.inventory_manager import InventoryManager
from inventory.menus import Menu



def main():
    """ 
    Main function to display the menu and handle user input. 
    
    Continuously displays a menu to the user and processes their input to execute 
    the corresponding tasks. 
    
    Validates that the user input is a number and calls the appropriate functions based on the chosen task number. 
    The loop continues until the user chooses to exit. 
    """
    inventory = InventoryManager()
    menu = Menu()
    menu.run_main_menu(inventory)

#run the programm
main()