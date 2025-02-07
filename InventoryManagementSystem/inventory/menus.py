import colors
from inventory.inventory_manager import InventoryManager
from inventory.products_manager import ProductManager
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
        Display the product menu options to the user. 

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
        """ 
        Display the inventory menu options to the user. 

        Prints a list of task options that the user can choose from. 
        """
        inventory_menu = ( 
        "==================================================\n"
        f"===        {colors.ANSI_BOLD}{colors.ANSI_GREEN}INVENTORY MANAGEMENT{colors.ANSI_RESET}      ===\n"
        "==================================================\n"
        f" {colors.ANSI_ITALIC}Please choose one of the following tasks:{colors.ANSI_RESET}\n"
        f" 1.    {colors.ANSI_UNDERLINE}Show inventory{colors.ANSI_RESET} \n"
        f" 2.    {colors.ANSI_UNDERLINE}Show products by category{colors.ANSI_RESET} \n"
        f" 3.    {colors.ANSI_UNDERLINE}Calculate the total inventory value{colors.ANSI_RESET} \n"
        f" 4.    {colors.ANSI_UNDERLINE}Sort the inventory{colors.ANSI_RESET} \n"
        f" 5.    {colors.ANSI_UNDERLINE}See total products value on bar graph{colors.ANSI_RESET} \n"
        f" 6.    {colors.ANSI_UNDERLINE}Show inventory products on pie graph{colors.ANSI_RESET} \n"
        f" 7.    {colors.ANSI_UNDERLINE}Save actual inventory to JSON{colors.ANSI_RESET} \n"
        f" 8.    {colors.ANSI_UNDERLINE}Load inventory from JSON{colors.ANSI_RESET} \n"
        f" 9.    {colors.ANSI_UNDERLINE}Go back{colors.ANSI_RESET}\n"
        "==================================================\n"
        )
        return inventory_menu
    def show_main_menu(self):
        """ 
        Show the main menu to the user.

        Returns the main menu string.
        """
        return self.main_menu
    def show_product_menu(self):
        """ 
        Show the product menu to the user.

        Returns the main menu string.
        """
        return self.product_menu
    def show_inventory_menu(self):
        """ 
        Show the inventory menu to the user.

        Returns the main menu string.
        """
        return self.inventory_menu

    def run_main_menu(self, inventory):
        """
        Display the main menu, validate user input, and execute corresponding tasks.

        Continuously displays the main menu to the user and processes their input to
        execute the corresponding tasks. Validates that the user input is an integer
        and calls the appropriate functions based on the chosen task number. The loop 
        continues until the user chooses to exit.

        Parameters:
        self: The instance of the Menu class.
        inventory: An instance of the InventoryManager class.
        """
        while True:
            print(self.show_main_menu())
            # Validate if the input is an integer 
            chosen_number = get_valid_input("What you want to do? ", "int")
            
            # Convert the input to an integer for task selection
            chosen_number = int(chosen_number) 

            if chosen_number == 1:
                print(self.show_product_menu())
                run_product_menu(self, inventory)
                keep_on()
            elif chosen_number == 2:
                print(self.show_inventory_menu())
                run_inventory_menu(self, inventory)
                keep_on()    
            elif chosen_number == 3:
                print("See you next time")
                exit()
            else:
                print("this option doesn't exist, try again")
def run_product_menu(self, inventory):
    """
    Display the product menu, validate user input, and execute corresponding tasks.

    Continuously displays the product menu to the user and processes their input to
    execute the corresponding tasks. Validates that the user input is an integer
    and calls the appropriate functions based on the chosen task number. The loop 
    continues until the user chooses to exit.

    Parameters:
    self: The instance of the Menu class.
    inventory: An instance of the InventoryManager class.
    """
    while True:
        print(self.show_product_menu())
        # Validate if the input is an integer 
        chosen_number = get_valid_input("What you want to do? ", "int")
        
        # Convert the input to an integer for task selection
        chosen_number = int(chosen_number) 

        if chosen_number == 1:
            ProductManager.add_product(inventory)
            keep_on()
        elif chosen_number == 2:
            name: str = show_input("Product",2, self.show_product_menu())
            ProductManager.delete_product(inventory, name)
            keep_on()
        elif chosen_number == 3:
            name: str = show_input("Product",3, self.show_product_menu())
            product_info = ProductManager.get_product_info(inventory, name)
            if product_info:
                print(product_info)
            keep_on()    
        elif chosen_number == 4:
            name: str = show_input("Product",4,self.show_product_menu())
            ProductManager.total_product_value(inventory, name)
            keep_on()
        elif chosen_number == 5:
            name: str = show_input("Product",5,self.show_product_menu())
            price: float = get_valid_input("New price ", "float")
            ProductManager.update_price(inventory, name, price)
            keep_on()
        elif chosen_number == 6:
            name: str = show_input("Product",6,self.show_product_menu())
            price: float = get_valid_input("New Quantity: ", "int")
            ProductManager.update_quantity(inventory, name, price)
            keep_on()
        elif chosen_number == 7:
            print(self.run_main_menu(inventory))
            keep_on()
        else:
            print("this option doesn't exist, try again")

def run_inventory_menu(self,inventory):
    """
    Display the inventory menu, validate user input, and execute corresponding tasks.

    Continuously displays the inventory menu to the user and processes their input to
    execute the corresponding tasks. Validates that the user input is an integer
    and calls the appropriate functions based on the chosen task number. The loop 
    continues until the user chooses to exit.

    Parameters:
    self: The instance of the Menu class.
    inventory: An instance of the InventoryManager class.
    """
    while True:
        print(self.show_inventory_menu())
        # Validate if the input is an integer 
        chosen_number = get_valid_input("What you want to do? ", "int")
        
        # Convert the input to an integer for task selection
        chosen_number = int(chosen_number) 
    
        if chosen_number == 1:
            """
            because show_inventory() don't need an input we can't use show_input() to print a title
            we have to hardcode a Title 'Inventory list:'
            """
            print(colors.ANSI_BLUE + "-"*20 + colors.ANSI_RESET)
            print(colors.ANSI_UNDERLINE + "Inventory list:" + colors.ANSI_RESET)
            print(colors.ANSI_BLUE + "-"*20 + colors.ANSI_RESET)
            InventoryManager.show_inventory(inventory)
            keep_on()
        elif chosen_number == 2:
            category: str = show_input("Category",2, self.show_inventory_menu())
            InventoryManager.product_summary_category(inventory, category)
            keep_on()
        elif chosen_number == 3:
            """
            because total_inventory_value() don't need an input we can't use show_input() to print a title
            we have to hardcode a Title 'Inventory list:'
            """
            print(colors.ANSI_BLUE + "-"*20 + colors.ANSI_RESET)
            print(colors.ANSI_UNDERLINE + "Total inventory value:" + colors.ANSI_RESET)
            print(colors.ANSI_BLUE + "-"*20 + colors.ANSI_RESET)
            InventoryManager.total_inventory_value(inventory)
            keep_on()
        elif chosen_number == 4:
            print(
                f'1. Sort by Name\n'
                f'2. Sort by Category\n'
                f'3. Sort by Price\n'
                f'4. Sort by Quantity\n'
            )
            option = get_valid_input("How do you want to sort? ", "int")
            option = int(option)
            if option == 1:
                sorted_inventory = InventoryManager.sort_by_attr(inventory,"name")
                InventoryManager.show_inventory(sorted_inventory)
            elif option == 2:
                sorted_inventory = InventoryManager.sort_by_attr(inventory,"category")
                InventoryManager.show_inventory(sorted_inventory)
            elif option == 3:
                sorted_inventory = InventoryManager.sort_by_attr(inventory,"price")
                InventoryManager.show_inventory(sorted_inventory)
            elif option == 4:
                sorted_inventory = InventoryManager.sort_by_attr(inventory,"quantity")
                InventoryManager.show_inventory(sorted_inventory)
            else:
                print("this option doesn't exist, try again")
            keep_on()
            print(run_inventory_menu(self,inventory)) 
        elif chosen_number == 5:
                InventoryManager.show_graph_product_value(inventory)
                keep_on()   
        elif chosen_number == 6:
                InventoryManager.show_pie_graph_products(inventory)
                keep_on()
        elif chosen_number == 7:
            file = show_input("File", 7, self.show_inventory_menu())
            InventoryManager.save_to_json(inventory, file)
            keep_on()
        elif chosen_number == 8:
            file = show_input("File", 8, self.show_inventory_menu())
            InventoryManager.load_from_json(inventory,file)
            keep_on()
        elif chosen_number == 9:
            print(self.run_main_menu(inventory))
            keep_on()          
        else:
            print("this option doesn't exist, try again")

def keep_on(): 
    """ 
    Pause the program to wait for user input to continue. 
    Prompts the user to press Enter to continue. 
    """ 
    input("\nPress Enter to continue...")