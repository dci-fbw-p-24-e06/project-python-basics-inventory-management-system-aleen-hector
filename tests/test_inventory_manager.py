import unittest
from unittest.mock import patch
from inventory.inventory_manager import InventoryManager
from inventory.product import Product  # Ensure you have your Product class imported

class TestInventoryManager(unittest.TestCase):

    def setUp(self):
        """Reset inventory before each test."""
        # Initialize InventoryManager in test mode so that interactive prompts are bypassed.
        self.inventory = InventoryManager(test_mode=True)
        self.inventory.clear_inventory()  # Ensure inventory is cleared

    @patch("builtins.input", side_effect=["yes", "+5"])
    def test_add_existing_product(self, mock_input):
        """Test that adding an existing product updates quantity when user confirms."""
        # First, add the product.
        self.inventory.add_product("Keyboard", "Electronics", 100, 5)
        # Adding the same product again should trigger the update prompt.
        self.inventory.add_product("Keyboard", "Electronics", 100, 5)
        # With side_effect ["yes", "+5"], the quantity should update: 5 + 5 = 10.
        self.assertEqual(self.inventory.products["Keyboard"].quantity, 10)

    def test_add_new_product(self):
        """Test adding a new product to the inventory."""
        self.inventory.add_product("Mouse", "Electronics", 50, 10)
        self.assertEqual(len(self.inventory.products), 1)
        self.assertEqual(self.inventory.products["Mouse"].name, "Mouse")

    def test_search_product_by_name(self):
        """Test searching for a product by name."""
        self.inventory.add_product("Webcam", "Electronics", 75, 12)
        results = self.inventory.search_product("Webcam")
        self.assertIsInstance(results, list)  # Ensure results is a list.
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Webcam")

    def test_search_product_case_insensitive(self):
        """Test searching for a product in a case-insensitive manner."""
        self.inventory.add_product("Gaming Mouse", "Electronics", 90, 5)
        results = self.inventory.search_product("gaming mouse")
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Gaming Mouse")

    def test_update_product_quantity(self):
        """Test updating the quantity of a product."""
        self.inventory.add_product("Headphones", "Electronics", 200, 15)
        self.inventory.update_quantity("Headphones", 25)
        self.assertEqual(self.inventory.products["Headphones"].quantity, 25)

    def test_update_quantity_of_non_existing_product(self):
        """Test that updating a non-existing product raises a ValueError in test mode."""
        with self.assertRaises(ValueError):
            self.inventory.update_quantity("NonExistingProduct", 10)

if __name__ == '__main__':
    unittest.main()

