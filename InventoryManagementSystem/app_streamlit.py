from inventory.product import Vegetable, Fruit, Electronic
from inventory.inventory_manager import InventoryManager
from inventory.products_manager import ProductManager
import streamlit as st
import pandas as pd

# Initialize ProductManager
product_manager = ProductManager()
inventory = InventoryManager()

#ADDING DATA 

# Vegetables
vegetable_data = [
    {"name": "Carrot", "price": 1.50, "quantity": 50, "expiry_date": "12/2025"},
    {"name": "Broccoli", "price": 2.00, "quantity": 30, "expiry_date": "01/2026"},
    {"name": "Spinach", "price": 1.25, "quantity": 40, "expiry_date": "11/2025"},
    {"name": "Potato", "price": 0.75, "quantity": 100, "expiry_date": "09/2025"}
]
for data in vegetable_data:
    new_vegetable = Vegetable.add_product(**data)
    inventory.add_product(new_vegetable)

# Fruits
fruit_data = [
    {"name": "Apple", "price": 0.50, "quantity": 100, "season": "Autumn"},
    {"name": "Banana", "price": 0.30, "quantity": 120, "season": "All year"},
    {"name": "Cherry", "price": 3.00, "quantity": 25, "season": "Summer"},
    {"name": "Orange", "price": 0.60, "quantity": 80, "season": "Winter"}
]
for data in fruit_data:
    new_fruit = Fruit.add_product(**data)
    inventory.add_product(new_fruit)

# Electronics
electronic_data = [
    {"name": "Laptop", "price": 999.99, "quantity": 10, "brand": "TechBrand", "warranty_period": 24},
    {"name": "Smartphone", "price": 699.99, "quantity": 20, "brand": "PhoneBrand", "warranty_period": 12},
    {"name": "Tablet", "price": 399.99, "quantity": 15, "brand": "TabBrand", "warranty_period": 18},
    {"name": "Headphones", "price": 199.99, "quantity": 30, "brand": "SoundBrand", "warranty_period": 12},
    {"name": "Smartwatch", "price": 299.99, "quantity": 25, "brand": "WatchBrand", "warranty_period": 24}
]
for data in electronic_data:
    new_electronic = Electronic.add_product(**data)
    inventory.add_product(new_electronic)

# Extract product data from inventory
inventory_data = []
for product in inventory.products:
    product_info = product.__dict__
    inventory_data.append(product_info)
# Convert data to a DataFrame
df = pd.DataFrame(inventory_data)

# Set the title
st.title('Inventory Display')

# Display the DataFrame as a table
st.write('Here is the current inventory:')
st.dataframe(df)
