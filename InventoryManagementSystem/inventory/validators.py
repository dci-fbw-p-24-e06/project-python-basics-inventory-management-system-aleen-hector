from .menus import show_main_menu
import colors

def number_validation(input_string: str, input_type: str):
    """
    Validate if the input string is a valid number of the given type.
    
    Parameters:
    input_string (str): The input string to validate.
    input_type (str): The type of number to validate ("int" or "float").
    
    Returns:
    bool: True if the input is a valid number of the given type, False otherwise.
    """
    try:
        if input_type == "int":
            int(input_string)
        elif input_type == "float":
            float(input_string)
        return True
    except ValueError:
        print(f"Error: Please enter a valid number.")
        return False

def get_valid_input(prompt: str, input_type: str):
    """
    Prompt the user for input and validate it as a number of the given type.
    
    Parameters:
    prompt (str): The prompt message to display to the user.
    input_type (str): The type of number to validate ("int" or "float").
    
    Returns:
    str: The valid input string.
    """
    while True:
        value = input(prompt)
        if number_validation(value, input_type):
            return value
        
def show_input(value: str, option:int ) -> str:
    menu_lines = show_main_menu().split('\n')
    print(colors.ANSI_BLUE + "-"*20 + colors.ANSI_RESET)
    print(menu_lines[option+3])
    print(colors.ANSI_BLUE + "-"*20 + colors.ANSI_RESET)
    type: str = input(f'Write the name of {value}: ')
    return type