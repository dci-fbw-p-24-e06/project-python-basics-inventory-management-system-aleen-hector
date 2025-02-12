import tkinter as tk
import subprocess
import os

def run_terminal_implementation():
    """
    Runs the terminal implementation of the Inventory Management System.

    This function prints a message indicating the start of the terminal
    implementation and then executes the main script of the Inventory 
    Management System using the subprocess module.

    The program runs with user data input and provides dynamic menus.
    """
    print("Running terminal implementation...")
    subprocess.run(["python3", "/home/dci-student/Projects/Python/Inventory_project/project-python-basics-inventory-management-system-aleen-hector/InventoryManagementSystem/main.py"])


def run_hard_data_implementation():
    """
    Runs the hard data testing implementation of the Inventory Management System.

    This function prints a message indicating the start of the hard data
    implementation and then executes the test script of the Inventory 
    Management System using the subprocess module. 

    The program runs testing hard code by calling all methods and printing 
    results directly on the terminal without any user interaction.
    """
    print("Running hard data implementation...")
    subprocess.run(["python3", "/home/dci-student/Projects/Python/Inventory_project/project-python-basics-inventory-management-system-aleen-hector/InventoryManagementSystem/test_inventory_manager.py"])


def run_gui_implementation():
    """
    Runs the GUI implementation of the Inventory Management System.

    This function prints a message indicating the start of the GUI
    implementation and then executes the GUI script of the Inventory 
    Management System using the subprocess module. 
    
    The program runs with a graphical user interface made with PySimpleGUI.
    """
    print("Running GUI implementation...")
    subprocess.run(["python3", "/home/dci-student/Projects/Python/Inventory_project/project-python-basics-inventory-management-system-aleen-hector/InventoryManagementGUI/main.py"])

def create_main_menu():
    """
    Creates the main menu for the Inventory Management System.

    This function sets up the main menu window using the tkinter module,
    which includes buttons for running the terminal implementation, hard 
    data implementation, and GUI implementation, as well as an exit button.
    """
    root = tk.Tk()
    root.title("Inventory Management System")

    label = tk.Label(root, text="INVENTORY MANAGEMENT SYSTEM", font=('Helvetica', 16))
    label.pack(pady=20)

    button_terminal = tk.Button(root, text="Terminal", font=('Helvetica', 12), command=run_terminal_implementation)
    button_terminal.pack(pady=10)

    button_hard_data = tk.Button(root, text="Hard Data Testing", font=('Helvetica', 12), command=run_hard_data_implementation)
    button_hard_data.pack(pady=10)

    button_gui = tk.Button(root, text="PySimpleGUI", font=('Helvetica', 12), command=run_gui_implementation)
    button_gui.pack(pady=10)

    button_exit = tk.Button(root, text="Exit", font=('Helvetica', 12), command=root.quit)
    button_exit.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_main_menu()
