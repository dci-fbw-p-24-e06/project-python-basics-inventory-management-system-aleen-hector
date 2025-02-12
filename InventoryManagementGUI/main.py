from inventory.product import Vegetable, Fruit, Electronic
from inventory.inventory_manager import InventoryManager
from inventory.products_manager import ProductManager
import PySimpleGUI as sg

from inventory.product import Vegetable, Fruit, Electronic
from inventory.inventory_manager import InventoryManager
from inventory.products_manager import ProductManager
   
if __name__ == "__main__":
   # Initialize ProductManager
   product_manager = ProductManager()
   inventory = InventoryManager()

# Initialize managers
product_manager = ProductManager()
inventory = InventoryManager()
class Menu:
    def __init__(self):
        self.main_menu = self.create_main_menu()

    def create_main_menu(self):
        layout = [
            [sg.Text('INVENTORY MANAGING SYSTEM', size=(30, 1), justification='center', font=('Helvetica', 16))],
            [sg.Text('Please choose one of the following tasks:', font=('Helvetica', 12))],
            [sg.Button('Products'), sg.Button('Inventory'), sg.Button('Exit')]
        ]
        return sg.Window('Main Menu', layout)

    def run_product_menu(self, inventory):
        layout = [
            [sg.Text('PRODUCT MANAGEMENT', size=(30, 1), justification='center', font=('Helvetica', 16), relief=sg.RELIEF_RIDGE)],
            [sg.Text('Please choose one of the following tasks:', font=('Helvetica', 12))],
            [sg.Button('Add product'), sg.Button('Remove product')],
            [sg.Button('Show product information'), sg.Button('Total product value')],
            [sg.Button('Update product price'), sg.Button('Update product quantity')],
            [sg.Button('Go back')]
        ]
        window = sg.Window('Product Menu', layout)
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Go back'):
                window.close()
                break
            elif event == 'Add product':
                product = product_manager.create_product()
                InventoryManager.add_product(inventory, product)
            elif event == 'Remove product':
                product_name = sg.popup_get_text('Enter the name of the product to remove:')
                if product_name:
                    ProductManager.delete_product(inventory, product_name)
            elif event == 'Show product information':
                product_name = sg.popup_get_text('Enter the name of the product:')
                if product_name:
                    ProductManager.get_product_info(inventory,product_name)
            elif event == 'Total product value':
                product_name = sg.popup_get_text('Enter the name of the product:')
                if product_name:
                    ProductManager.total_product_value(inventory, product_name)
            elif event == 'Update product price':
                product_name = sg.popup_get_text('Enter the name of the product:')
                if product_name:
                    ProductManager.update_price(inventory, product_name)
            elif event == 'Update product quantity':
                product_name = sg.popup_get_text('Enter the name of the product:')
                ProductManager.update_quantity(inventory, product_name) 

    def run_inventory_menu(self, inventory):
        layout = [
            [sg.Text('INVENTORY MANAGEMENT', size=(30, 1), justification='center', font=("Helvetica", 16), relief=sg.RELIEF_RIDGE)],
            [sg.Text('Please choose one of the following tasks:', font=("Helvetica", 12))],
            [sg.Button('Show inventory'), sg.Button('Show products by category')],
            [sg.Button('Calculate the total inventory value'), sg.Button('Sort the inventory')],
            [sg.Button('See total products value on bar graph'), sg.Button('Show inventory products on pie graph')],
            [sg.Button('Save actual inventory to JSON'), sg.Button('Load inventory from JSON')],
            [sg.Button('Go back')]
        ]
        window = sg.Window('Inventory Menu', layout)
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Go back'):
                window.close()
                break
            elif event == 'Show inventory':
                inventory.show_inventory()
            elif event == 'Show products by category':
                inventory.product_summary_category()
            elif event == 'Calculate the total inventory value':
                inventory.total_inventory_value()
            elif event == 'Sort the inventory':
                sort_layout = [
                    [sg.Text('Sort by:'), sg.Button('Name'), sg.Button('Category'), sg.Button('Price'), sg.Button('Quantity')]
                ]
                sort_window = sg.Window('Sort Inventory', sort_layout)
                sort_event, sort_values = sort_window.read()
                if sort_event in ('Name', 'Category', 'Price', 'Quantity'):
                    sorted_inventory = InventoryManager.sort_by_attr(inventory, sort_event.lower())
                    inventory.show_inventory(sorted_inventory)
                sort_window.close()
            elif event == 'See total products value on bar graph':
                inventory.show_graph_product_value()
            elif event == 'Show inventory products on pie graph':
                inventory.show_pie_graph_products()
            elif event == 'Save actual inventory to JSON':
                    inventory.save_to_json()
            elif event == 'Load inventory from JSON':
                file = sg.popup_get_file('Load from file', no_window=True)
                if file:
                    inventory.load_from_json(file)


def main():
    menu = Menu()
    window = menu.create_main_menu()
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Products':
            window.hide()
            menu.run_product_menu(inventory)
            window.un_hide()
        elif event == 'Inventory':
            window.hide()
            menu.run_inventory_menu(inventory)
            window.un_hide()
    window.close()

if __name__ == "__main__":
    main()

