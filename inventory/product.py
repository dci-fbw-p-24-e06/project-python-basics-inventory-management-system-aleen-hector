class Product:
    """Represents a product in the directory"""

    def __init__(self, name: str, category: str, price: float, quantity: int):
        """Initialize a product with given name, category, price, and quantity.
        Parameters:
        name (str): Name of the product
        category (str): Category of the product
        price (float): Price of the product in euros
        quantity (int): Available quantity of the product
        """
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """Returns a string representation of the product."""
        return (
            f"Product: {self.name}, Category: {self.category}, "
            f"Price: {self.price} €, Quantity: {self.quantity}"
        )

    def update_quantity(self, new_quantity: int) -> int:
        """Updates the quantity of the product"""
        self.quantity = new_quantity
        return self.quantity

    def update_price(self, new_price: float) -> float:
        """Updates the price of the product"""
        self.price = new_price
        return self.price

    def decrease_quantity(self, quantity):
        """Decreases the quantity of the product by the given amount

        Parameters:
        quantity (int): Amount to decrease from stock.
        raises ValueError: If quantity to decrease is greater than stock.
        Returns:
        int: The remaining quantity after decrease."""
        if self.quantity - quantity < 0:
            raise ValueError(
                f"Cannot decrease quantity beyond stock for {self.name}")
        self.quantity -= quantity
        return self.quantity

    def calculate_total_value(self) -> float:
        """Calculates the total value of the product (price x quantity)"""
        return self.price * self.quantity

    def get_product_info(self) -> str:
        """Returns a formated string containing product details"""
        return (
            f"Product: {self.name}, Category:{self.category}, "
            f"Price: {self.price} €, Quantity: {self.quantity}"
        )
