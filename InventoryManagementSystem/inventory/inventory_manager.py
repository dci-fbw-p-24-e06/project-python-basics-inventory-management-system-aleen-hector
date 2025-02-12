from inventory.product import Product, Electronic, Vegetable, Fruit
import json
import matplotlib.pyplot as plt
import numpy as np
class InventoryManager:
    def __init__(self,products = []):
        """
        Initialize the InventoryManager with a list of products.
        
        Parameters:
        products (list): A list of Product objects. Defaults to an empty list if not provided.
        """
        self.products = products
    
    def is_inventory_empty(func):
        """
        Decorator to check if the inventory is empty.

        If the inventory is empty, it prints "Inventory is empty" and returns None.
        Otherwise, it calls the decorated function.

        Parameters:
        func: The function to be decorated.

        Returns:
        inner: The decorated function.
        """
        def inner(self, *args, **kwargs):
            if not self or not self.products:
                print("Inventory is empty")
                return None
            return func(self, *args, **kwargs)
        return inner


    def find_product(self, product_name: str) -> Product:
        """
        Find a product in the inventory by name.
        
        Parameters:
        product_name (str): The name of the product to find.
        
        Returns:
        Product: The Product object if found, None otherwise.
        """
        for product in self.products:
            if product.name == product_name:
                return product
        return None
    
    def add_product(self,product):
        """
        Add a product to the inventory if it doesn't already exist.

        This method checks if a product with the same name already exists in the inventory.
        If it doesn't, the product is added to the inventory. If it does, a message is 
        printed indicating that the product already exists.

        Args:
            product (Product): The product to be added to the inventory.

        Returns:
            Product: The added product if it was successfully added.
            None: If the product already exists in the inventory.
        """
        if not self.find_product(product.name):
            self.products.append(product)
            print(f"{product.name} added succesfully")
            return product
        else:
            print("Product already exists in the inventory")
            return None
        
    @is_inventory_empty
    def show_inventory(self):
        """
        Print the inventory with product information.

        Iterates through the products in the inventory and prints the information of each product.
        """
        for product in self.products:
            print(product.print_product_info())
        return self

    @is_inventory_empty
    def product_summary_category(self, category: str):
        """
        Print a summary of products in the specified category.

        Iterates through the products in the inventory and collects the names of
        products that belong to the specified category. If there are no products
        in the specified category, it prints a message indicating so. Otherwise,
        it prints the names of the products in the category.

        Parameters:
        self: The instance of the Inventory class.
        category (str): The category to summarize.

        Returns:
        self: The instance of the Inventory class.
        """
        list_products = []
        for product in self.products:
            if product.category == category:
                list_products.append(product.name)
        if not list_products:
            print("This category doesn't exists already or have not products")
        else:
            print(", ".join(list_products))
        return self
    
    @is_inventory_empty
    def total_inventory_value(self):
        """
        Calculate and print the total inventory value.

        Sums up the value of all products in the inventory (price * quantity) and prints the total value in euros.
        If the inventory is empty, it returns None.

        Returns:
        self: The instance of the Inventory class.
        """
        total_value = sum(product.price * product.quantity for product in self.products)
        print(f"Total inventory value = {total_value} €")
        return self
        
    @is_inventory_empty
    def save_to_json(self, filename):
        """
        Save the inventory data to a JSON file.
        
        Parameters:
        filename (str): The name of the file to save the inventory data to.
        """
        with open(filename, 'w') as file:
            json.dump([product.to_dict() for product in self.products], file, indent=3)
        print(f"Inventory saved to {filename}")

    def load_from_json(self, filename):
        """
        Load the inventory data from a JSON file.
        In this method, product_class_mapping map the category names to their corresponding classes in a dictionary. 
        This allows the method to create instances of the correct subclass based on the category field in the JSON data.
        
        Parameters:
        filename (str): The name of the file to load the inventory data from.
        """
        product_class_mapping = {
            'Fruit': Fruit,
            'Vegetable': Vegetable,
            'Electronic': Electronic
        }
        
        try:
            with open(filename, 'r') as file:
                products_data = json.load(file)
                self.products = []
                for data in products_data:
                    category = data['category']
                    product_class = product_class_mapping.get(category, Product)
                    self.products.append(product_class(**data))
            print(f"Inventory loaded from {filename}")
        except FileNotFoundError:
            print(f"No such file: {filename}")

    
    def sort_by_attr(self, attr):
        """
        Sort the products by a specified attribute.

        Parameters
        attr: The attribute name by which to sort the products

        Return: A new InventoryManager instance with sorted products
        """
        self.products.sort(key= lambda x: getattr(x, attr))
        sorted_inventory = InventoryManager(self.products)
        return sorted_inventory


### GRAPHICAL VISUALIZATION IMPLEMENTING ###


    def show_pie_graph_products(self):
        """
        Displays a pie chart of the quantities of products.

        This function creates a pie chart that shows the distribution of product quantities
        in the inventory. A legend is added outside the pie chart to display the product names
        and their corresponding quantities.

        Args:
            self: An instance of the class containing product data.

        Attributes:
            self.products (list): A list of product objects, each having attributes 'name', 'price', and 'quantity'.

        Returns:
            None
        """
        quantities = []
        product_names = []
        for product in self.products:
            quantities.append(product.quantity)
            product_names.append(product.name)
        plt.figure(figsize=(10, 7))
        wedges, texts = plt.pie(quantities, labels=None)

        plt.title("Products in the Inventory")

        # Add legend outside the pie chart
        # The bbox_to_anchor parameter helps position the legend outside the chart.
        plt.legend(wedges, [f'{name}: {quantity}' for name, quantity in zip(product_names, quantities)],
               title="Products and Quantities",
               loc="center left",
               bbox_to_anchor=(1, 0, 0.5, 1))
        plt.show()
    
    def show_graph_product_value(self):
        """
        Displays bar graphs of the total value of products.

        This function calculates the total value of each product (price multiplied by quantity)
        and sorts the products based on their total value in descending order. It then creates
        two subplots: one for products with a total value of 300 or more, and one for products
        with a total value less than 300. The bar graphs display the product names and their 
        corresponding total values.

        Args:
            self: An instance of the class containing product data.

        Attributes:
            self.products (list): A list of product objects, each having attributes 'name', 'price', and 'quantity'.

        Returns:
            None
        """
        # Calculate total product values and sort products by total value
        self.products.sort(key=lambda product: product.price * product.quantity, reverse=True)
        product_values_high = []
        product_names_high = []
        product_values_low = []
        product_names_low = []

        for product in self.products:
            total_product_value: float = product.price * product.quantity
            if total_product_value < 300:
                product_values_low.append(total_product_value)
                product_names_low.append(product.name)
            else:
                product_values_high.append(total_product_value)
                product_names_high.append(product.name)

        # Create subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 4))

        # Plot high-value products
        bars1 = ax1.barh(product_names_high, product_values_high, height=0.7)
        ax1.set_title("Products with Total Value ≥ 300")
        ax1.set_xlabel("Total Value (€)")
        ax1.spines[['right', 'top', 'bottom']].set_visible(False)
        ax1.xaxis.set_visible(False)
        ax1.bar_label(bars1, padding=-60, color='white', 
                      fontsize=10, fontweight='bold', fmt='%.1f €')
        
        # Plot low-value products
        bars2 = ax2.barh(product_names_low, product_values_low, height=0.7)
        ax2.set_title("Products with Total Value < 300")
        ax2.set_xlabel("Total Value (€)")
        ax2.spines[['right', 'top', 'bottom']].set_visible(False)
        ax2.xaxis.set_visible(False)
        ax2.bar_label(bars2, padding=-45, color='white', 
                      fontsize=10, fontweight='bold', fmt='%.1f €')

        #show the plot
        plt.show()

    