from inventory.product import Product, Electronic, Vegetable, Fruit
import PySimpleGUI as sg

def get_subclasses(cls):
    subclasses = cls.__subclasses__()
    list_subclasses = []
    for subclass in subclasses:
        subclasses.extend(get_subclasses(subclass))
        list_subclasses.append(subclass.__name__)
    return list_subclasses

class ProductManager:

    def __init__(self):
        self.products = []

    def check_product_exists(func):
        def inner(self, name, *args, **kwargs):
            product = self.find_product(name)
            if not product:
                sg.popup("Product not found")
                return None
            return func(self, name, *args, **kwargs)
        return inner
    
    def create_product(self):
        all_subclasses = get_subclasses(Product)
        layout = [
            [sg.Text(f"Choose a category: {all_subclasses}")],
            [sg.InputText(key='CATEGORY')],
            [sg.Button('Submit')]
        ]
        window = sg.Window('Add Product', layout)
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED,):
                window.close()
                return
            category = values['CATEGORY']
            if category not in all_subclasses:
                sg.popup("Category doesn't exist, try again")
            else:
                break
        window.close()

        if category == "Electronic":
            data = Electronic.get_user_input()
            product = Electronic.add_product(**data)
        elif category == "Vegetable":
            data = Vegetable.get_user_input()
            product = Vegetable.add_product(**data)
        elif category == "Fruit":
            data = Fruit.get_user_input()
            product = Fruit.add_product(**data)
        return product

    def find_product(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None
    
    @check_product_exists
    def delete_product(self, name):
        product = self.find_product(name)
        self.products.remove(product)
        sg.popup(f"Product {product.name} found and deleted from inventory")
        return self
    
    @check_product_exists
    def get_product_info(self, name):
        product = self.find_product(name)

        summary = product.print_product_info()

        layout = [
            [sg.Text('Product Information')],
            [sg.Multiline(summary, size=(100, 10), disabled=True, autoscroll=True)],
            [sg.Button('Close')]
        ]
        window = sg.Window('Product Information', layout, finalize=True)

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Close'):
                break

        window.close()
    
    @check_product_exists
    def update_price(self, name):
        """
        Update the price of an existing product using a GUI.

        This method finds the product by name, prompts the user to enter a new price,
        validates the input, and updates the product's price if the input is valid.

        Args:
        name (str): The name of the product to update.

        Returns:
        self: The instance of the class with the updated product price.
        """
        product = self.find_product(name)
        while True:
            new_price = sg.popup_get_text('Enter the new price:')
            try:
                new_price = float(new_price)
                product.price = new_price
                sg.popup(f"Price of {name} updated to {product.price}")
                return self
            except ValueError:
                sg.popup_error("Please enter a valid float value for the price.")
    
    @check_product_exists
    def update_quantity(self, name):
        product = self.find_product(name)
        while True:
            new_quantity = sg.popup_get_text('Enter the new quantity:')
            try:
                product.quantity = int(new_quantity)
                sg.popup(f"Quantity of {name} updated to {product.quantity}")
                return self
            except ValueError:
                sg.popup_error("Please enter a valid int value for the price.")
    
    @check_product_exists
    def total_product_value(self, name):
        product = self.find_product(name)
        total_value:float  = float(product.price) * int(product.quantity)
        sg.popup(f"The total value of {product.name} is: {total_value} euros")
        return total_value