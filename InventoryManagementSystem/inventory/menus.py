import colors
def show_main_menu():
    """ 
    Display the menu options to the user. 

    Prints a list of task options that the user can choose from. 
    """
    main_menu = ( 
     "==================================================\n"
    f"===        {colors.ANSI_BOLD}{colors.ANSI_GREEN}INVENTORY MANAGING SYSTEM{colors.ANSI_RESET}      ===\n"
    "==================================================\n"
    f" {colors.ANSI_ITALIC}Please choose one of the following tasks:{colors.ANSI_RESET}\n"
    f" 1.    {colors.ANSI_UNDERLINE}Add product{colors.ANSI_RESET} \n"
    f" 2.    {colors.ANSI_UNDERLINE}Remove product{colors.ANSI_RESET} \n"
    f" 3.    {colors.ANSI_UNDERLINE}See product information{colors.ANSI_RESET} \n"
    f" 4.    {colors.ANSI_UNDERLINE}See inventory{colors.ANSI_RESET} \n"
    f" 5.    {colors.ANSI_UNDERLINE}Total Product Value{colors.ANSI_RESET} \n"
    f" 6.    {colors.ANSI_UNDERLINE}See products by category{colors.ANSI_RESET} \n"
    f" 18.   {colors.ANSI_UNDERLINE}Save inventory to JSON{colors.ANSI_RESET} \n"
    f" 19.   {colors.ANSI_UNDERLINE}Load inventory from JSON{colors.ANSI_RESET} \n"
    f" 20.   {colors.ANSI_UNDERLINE}Exit{colors.ANSI_RESET}\n"
    "==================================================\n"
    )
    return main_menu

def show_products_menu():
    """ 
    Display the menu options to the user. 

    Prints a list of task options that the user can choose from. 
    """
    products_menu = ( 
     "==================================================\n"
    f"===        {colors.ANSI_BOLD}{colors.ANSI_GREEN}PRODUCTS{colors.ANSI_RESET}      ===\n"
    "==================================================\n"
    f" {colors.ANSI_ITALIC}Please choose one of the following tasks:{colors.ANSI_RESET}\n"
    f" 1.    {colors.ANSI_UNDERLINE}Add product{colors.ANSI_RESET} \n"
    f" 2.    {colors.ANSI_UNDERLINE}Remove product{colors.ANSI_RESET} \n"
    f" 3.    {colors.ANSI_UNDERLINE}See product information{colors.ANSI_RESET} \n"
    f" 4.    {colors.ANSI_UNDERLINE}Total Product Value{colors.ANSI_RESET} \n"
    f" 5.    {colors.ANSI_UNDERLINE}Update product price{colors.ANSI_RESET} \n"
    f" 6.    {colors.ANSI_UNDERLINE}Update product Quantity{colors.ANSI_RESET} \n" 
    f" 7.    {colors.ANSI_UNDERLINE}Go Back{colors.ANSI_RESET}\n"
    "==================================================\n"
    )
    return products_menu