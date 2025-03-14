import unittest
from inventory.inventory_manager import InventoryManager

class TestInventoryManager(unittest.TestCase):

    def setUp(self):
        """Set up a fresh inventory instance before each test."""
        self.inventory = InventoryManager()

    def test_add_new_product(self):
        """Test adding a new product to the inventory."""
        self.inventory.add_product("Mouse", "Electronics", 50, 10)
        self.assertIn("Mouse", self.inventory.products)
        self.assertEqual(self.inventory.products["Mouse"].price, 50)
        self.assertEqual(self.inventory.products["Mouse"].quantity, 10)

    def test_add_existing_product(self):
        """Test that adding an existing product raises a ValueError."""
        self.inventory.add_product("Keyboard", "Electronics", 100, 5)
        with self.assertRaises(ValueError):
            self.inventory.add_product("Keyboard", "Electronics", 100, 3)

    def test_remove_product(self):
        """Test removing a product from inventory."""
        self.inventory.add_product("Monitor", "Electronics", 300, 8)
        self.inventory.remove_product("Monitor")
        self.assertNotIn("Monitor", self.inventory.products)

    def test_remove_non_existing_product(self):
        """Test that removing a non-existing product raises a ValueError."""
        with self.assertRaises(ValueError):
            self.inventory.remove_product("Speakers")

    def test_update_product_quantity(self):
        """Test updating the quantity of a product."""
        self.inventory.add_product("Headphones", "Electronics", 200, 15)
        self.inventory.update_quantity("Headphones", 25)
        self.assertEqual(self.inventory.products["Headphones"].quantity, 25)

    def test_update_quantity_of_non_existing_product(self):
        """Test that updating a non-existing product's quantity raises a ValueError."""
        with self.assertRaises(ValueError):
            self.inventory.update_quantity("Tablet", 20)

    def test_search_product_by_name(self):
        """Test searching for a product by name."""
        self.inventory.add_product("Webcam", "Electronics", 75, 12)
        results = self.inventory.search_product("Webcam")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Webcam")

    def test_search_product_case_insensitive(self):
        """Test searching for a product in a case-insensitive manner."""
        self.inventory.add_product("Gaming Mouse", "Electronics", 90, 5)
        results = self.inventory.search_product("gaming mouse")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Gaming Mouse")

if __name__ == '__main__':
    unittest.main()
