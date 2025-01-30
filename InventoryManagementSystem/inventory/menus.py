import colors
from inventory.inventory_manager import InventoryManager
from inventory.product import Product
from inventory.validators import get_valid_input, show_input
class Menu:
    def __init__(self):
        self.main_menu = self.create_main_menu()
        self.product_menu = self.create_product_menu()
        self.inventory_menu = self.create_inventory_menu()
    def create_main_menu(self):
        """ 
        Display the main menu options to the user when program runs. 

        Prints a list of task options that the user can choose from. 
        """
        main_menu =  ( 
        "==================================================\n"
        f"===        {colors.ANSI_BOLD}{colors.ANSI_GREEN}INVENTORY MANAGING SYSTEM{colors.ANSI_RESET}      ===\n"
        "==================================================\n"
        f" {colors.ANSI_ITALIC}Please choose one of the following tasks:{colors.ANSI_RESET}\n"
        f" 1.    {colors.ANSI_UNDERLINE}Products{colors.ANSI_RESET} \n"
        f" 2.    {colors.ANSI_UNDERLINE}Inventory{colors.ANSI_RESET} \n"
        f" 3.    {colors.ANSI_UNDERLINE}Exit{colors.ANSI_RESET} \n"
        "==================================================\n"
        )
        return main_menu

    def create_product_menu(self):
        """ 
        Display the menu options to the user. 

        Prints a list of task options that the user can choose from. 
        """
        product_menu = ( 
        "==================================================\n"
        f"===        {colors.ANSI_BOLD}{colors.ANSI_GREEN}PRODUCT MANAGEMENT{colors.ANSI_RESET}      ===\n"
        "==================================================\n"
        f" {colors.ANSI_ITALIC}Please choose one of the following tasks:{colors.ANSI_RESET}\n"
        f" 1.    {colors.ANSI_UNDERLINE}Add product{colors.ANSI_RESET} \n"
        f" 2.    {colors.ANSI_UNDERLINE}Remove product{colors.ANSI_RESET} \n"
        f" 3.    {colors.ANSI_UNDERLINE}Show product information{colors.ANSI_RESET} \n"
        f" 4.    {colors.ANSI_UNDERLINE}Total product value{colors.ANSI_RESET} \n"
        f" 5.    {colors.ANSI_UNDERLINE}Update product price{colors.ANSI_RESET} \n"
        f" 6.    {colors.ANSI_UNDERLINE}Update product quantity{colors.ANSI_RESET} \n" 
        f" 7.    {colors.ANSI_UNDERLINE}Go back{colors.ANSI_RESET}\n"
        "==================================================\n"
        )
        return product_menu

    def create_inventory_menu(self):
        inventory_menu = ( 
        "==================================================\n"
        f"===        {colors.ANSI_BOLD}{colors.ANSI_GREEN}INVENTORY MANAGEMENT{colors.ANSI_RESET}      ===\n"
        "==================================================\n"
        f" {colors.ANSI_ITALIC}Please choose one of the following tasks:{colors.ANSI_RESET}\n"
        f" 1.    {colors.ANSI_UNDERLINE}Show inventory{colors.ANSI_RESET} \n"
        f" 2.    {colors.ANSI_UNDERLINE}Search products by category{colors.ANSI_RESET} \n"
        f" 3.    {colors.ANSI_UNDERLINE}Calculate the total inventory value{colors.ANSI_RESET} \n"
        f" 10.   {colors.ANSI_UNDERLINE}Save actual inventory to JSON{colors.ANSI_RESET} \n"
        f" 11.   {colors.ANSI_UNDERLINE}Load inventory from JSON{colors.ANSI_RESET} \n"
        f" 12.   {colors.ANSI_UNDERLINE}Go back{colors.ANSI_RESET}\n"
        "==================================================\n"
        )
        return inventory_menu
    def show_main_menu(self):
        return self.main_menu
    def show_product_menu(self):
        return self.product_menu
    def show_inventory_menu(self):
        return self.inventory_menu

    def run_main_menu(self, inventory):
        while True:
            print(self.show_main_menu())
            # Validate if the input is an integer 
            chosen_number = get_valid_input("What you want to do? ", "int")
            
            # Proceed with the task selection
            chosen_number = int(chosen_number) 

            if chosen_number == 1:
                print(self.show_product_menu())
                run_product_menu(self, inventory)
                keepOn()
            elif chosen_number == 2:
                print(self.show_inventory_menu())
                run_inventory_menu(self, inventory)
                keepOn()    
            elif chosen_number == 3:
                print("See you next time")
                exit()
            else:
                print("this option doesn't exist, try again")
def run_product_menu(self, inventory):
    while True:
        print(self.show_product_menu())
        # Validate if the input is an integer 
        chosen_number = get_valid_input("What you want to do? ", "int")
        
        # Proceed with the task selection
        chosen_number = int(chosen_number) 

        if chosen_number == 1:
            name: str = show_input("Product",1, self.show_product_menu())
            Product.add_product(inventory, name)
            keepOn()
        elif chosen_number == 2:
            name: str = show_input("Product",2, self.show_product_menu())
            Product.delete_product(inventory, name)
            keepOn()
        elif chosen_number == 3:
            name: str = show_input("Product",3, self.show_product_menu())
            product_info = Product.get_product_info(inventory, name)
            if product_info:
                print(product_info)
            keepOn()    
        elif chosen_number == 4:
            name: str = show_input("Product",4,self.show_product_menu())
            Product.total_product_value(inventory, name)
            keepOn()
        elif chosen_number == 5:
            name: str = show_input("Product",5,self.show_product_menu())
            price: float = float(input("new price: "))
            Product.update_price(inventory, name, price)
            keepOn()
        elif chosen_number == 6:
            name: str = show_input("Product",6,self.show_product_menu())
            price: float = input("new Quantity: ")
            Product.update_quantity(inventory, name, price)
            keepOn()
        elif chosen_number == 7:
            print(self.run_main_menu(inventory))
            keepOn()
        else:
            print("this option doesn't exist, try again")

def run_inventory_menu(self,inventory):
    while True:
        print(self.show_inventory_menu())
        # Validate if the input is an integer 
        chosen_number = get_valid_input("What you want to do? ", "int")
        
        # Proceed with the task selection
        chosen_number = int(chosen_number) 
    
        if chosen_number == 1:
            print("Inventory list:")
            print("*"*20)
            InventoryManager.show_inventory(inventory)
            keepOn()
        elif chosen_number == 2:
            category: str = show_input("Category",2, self.show_inventory_menu())
            InventoryManager.product_summary_category(inventory, category)
            keepOn()
        elif chosen_number == 3:
            print("Total inventory value:")
            print("*"*20)
            InventoryManager.total_inventory_value(inventory)
            keepOn()
        elif chosen_number == 10:
            file = show_input("File", 4, self.show_inventory_menu())
            InventoryManager.save_to_json(inventory, file)
            keepOn()
        elif chosen_number == 11:
            file = show_input("File", 5, self.show_inventory_menu())
            InventoryManager.load_from_json(inventory,file)
            keepOn()
        elif chosen_number == 12:
            print(self.run_main_menu(inventory))
            keepOn()            
        else:
            print("this option doesn't exist, try again")

def keepOn(): 
    """ 
    Pause the program to wait for user input to continue. 
    Prompts the user to press Enter to continue. 
    """ 
    input("\nPress Enter to continue...")