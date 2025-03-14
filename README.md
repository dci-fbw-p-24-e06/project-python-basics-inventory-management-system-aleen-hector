# Inventory Management System

## Overview
The **Inventory Management System** is a simple Python-based application that allows users to manage a store's inventory efficiently. The system supports adding, removing, updating products, retrieving product information, and calculating the total value of the inventory. Additionally, it loads product data from a JSON file and displays inventory in a color-coded table.

## Features
- 🛒 **Product Management**: Add, remove, update product details.
- 📊 **Inventory Display**: View products in a visually appealing color-coded table.
- 💰 **Total Value Calculation**: Compute the total worth of inventory.
- 📂 **Data Loading**: Load product details from a JSON file.
- ✅ **Unit Testing**: Ensures reliability using the `unittest` module.

## Project Structure
```plaintext
InventoryManagementSystem/
├── inventory/
│   ├── __init__.py
│   ├── product.py
│   ├── inventory_manager.py
│   ├── inventory_data.json  # JSON database with categorized products
├── tests/
│   ├── __init__.py
│   ├── test_inventory_manager.py
├── main.py
├── README.md
├── requirements.txt
```

## Installation
### Prerequisites
Ensure you have **Python 3.7+** installed on your system.

### Install Dependencies
```sh
pip install -r requirements.txt
```

## Usage
### 1️⃣ Load Inventory from JSON and Display
Run the main program to load products from `inventory_data.json` and view them in a color-coded table.
```sh
python main.py
```

### 2️⃣ Running Unit Tests
To validate functionality, execute the test suite:
```sh
python -m unittest discover tests
```

## Technologies Used
- **Python 3** – Core programming language
- **JSON** – Data storage for product information
- **Tabulate** – Table formatting for beautiful inventory display
- **Colorama** – Color-coded categories in terminal output
- **Unittest** – Unit testing framework

## Example Inventory Display
```
╒════════════════╤═════════════════╤═══════════╤══════════╕
│ Product Name   │ Category        │ Price     │ Quantity │
╞════════════════╪═════════════════╪═══════════╪══════════╡
│ Laptop        │ Electronics     │ $1200.00  │ 10       │
│ T-shirt       │ Clothing        │ $20.00    │ 100      │
│ Milk          │ Groceries       │ $3.00     │ 200      │
│ Couch         │ Home Essentials │ $500.00   │ 5        │
╘════════════════╧═════════════════╧═══════════╧══════════╛
```

## Future Enhancements
🔹 **Search functionality** to find products quickly.  
🔹 **Export reports** in CSV or Excel format.  
🔹 **GUI Integration** using Tkinter or Flask for web-based management.

## License
This project is licensed under the **MIT License**.

---
