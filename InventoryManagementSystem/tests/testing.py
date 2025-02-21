import unittest
from inventory.product import Vegetable, Fruit, Electronic, Product
from inventory.inventory_manager import InventoryManager
from inventory.products_manager import ProductManager, get_subclasses
import colors

class TestInventoryManager(unittest.TestCase):
    
    def setUp(self):
        self.inventory = InventoryManager()
        self.orange = Fruit.create_product(name="Orange", price=0.50, quantity=80, season="Winter")
        #create Fruit instances
        self.apple = Fruit.create_product(name="Apple", price=1, quantity=100, season="Autumn") 
        self.banana = Fruit.create_product(name="Banana", price=0.50, quantity=50, season="All year") 
        self.cherry = Fruit.create_product(name="Cherry", price=2.00, quantity=25, season="Summer") 
        self.strawberry = Fruit.create_product(name="Strawberry", price=1.50, quantity=10, season="Spring") 
        self.grape = Fruit.create_product(name="Grape", price=2.50, quantity=40, season="Autumn") 
        #add Fruits to the inventory
        self.inventory.add_product(self.apple)
        self.inventory.add_product(self.banana)
        self.inventory.add_product(self.cherry)
        self.inventory.add_product(self.strawberry)
        self.inventory.add_product(self.grape)
    def test_is_inventory_empty(self):
        self.assertTrue(self.inventory.is_inventory_empty())
    def test_find_product(self):
        self.assertIsNone(self.inventory.find_product("Carrot"))
    def test_add_product(self):
        self.assertEqual(self.inventory.add_product(self.orange),self.orange)
    def test_add_product_already_exists(self):
        self.inventory.add_product(self.orange)
        self.assertEqual(self.inventory.add_product(self.orange),None)
    def test_product_summary_categories(self):
        self.assertListEqual(self.inventory.product_summary_category("Fruit"), ["Apple", "Banana", "Cherry", "Strawberry", "Grape"])
    def test_total_inventory_value(self):
        self.assertEqual(self.inventory.total_inventory_value(), 290)
    def test_show_inventory(self):
        product_list = [product.name for product in self.inventory.show_inventory()]
        self.assertIn("Banana", product_list)
        self.assertIn("Cherry", product_list)
        self.assertIn("Grape", product_list)
        self.assertIn("Strawberry", product_list)
        self.assertIn("Apple", product_list)
    def tearDown(self):
        self.inventory = InventoryManager()



class TestProductsManager(unittest.TestCase):
    
    def setUp(self):
        self.product_manager = ProductManager()
        self.inventory = InventoryManager()

        # Vegetable object instance
        self.tomato = Vegetable.create_product(name="Tomato", price=2.00, quantity=50, expiry_date="10/2025")
        # Fruit object instance
        self.strawberry = Fruit.create_product(name="Strawberry", price=0.20, quantity=200, season="Summer")
        
        # Electronic object instance
        self.camera = Electronic.create_product(name="Camera", price=500, quantity=10, brand="PhotoBrand", warranty_period=12)

        self.inventory.add_product(self.tomato)
        self.inventory.add_product(self.strawberry)
        self.inventory.add_product(self.camera)
    def test_get_suclasses(self):
        all_subclasses = get_subclasses(Product)
        self.assertListEqual(all_subclasses, ["Vegetable", "Fruit", "Electronic"])

    def test_delete_product(self):
        

        ProductManager.delete_product(self.inventory, "Camera")
        self.assertIsNone(self.inventory.find_product("Camera"))
        product_list = [product.name for product in self.inventory.show_inventory()]
        self.assertNotIn("Camera", product_list)
    
    def test_get_product_info(self):
        expected_output = expected_output = (f"{colors.ANSI_CYAN}Name{colors.ANSI_RESET}: Tomato       "
                   f"{colors.ANSI_CYAN}Category{colors.ANSI_RESET}: Vegetable    "
                   f"{colors.ANSI_CYAN}Price{colors.ANSI_RESET}: 2.0          "
                   f"{colors.ANSI_CYAN}Quantity{colors.ANSI_RESET}: 50           "
                   f"{colors.ANSI_CYAN}Expiry_date{colors.ANSI_RESET}: 10/2025     ")
        actual_output = ProductManager.get_product_info(self.inventory, "Tomato")
        self.assertEqual(actual_output, expected_output)
    
    def test_update_price(self):
        self.assertEqual(ProductManager.update_price(self.inventory,"Strawberry", 2), 2)
    def test_update_quantity(self):
        self.assertEqual(ProductManager.update_quantity(self.inventory,"Strawberry", 20), 20)
    def test_total_product_value(self):
        self.inventory.add_product(self.camera)
        self.assertEqual(ProductManager.total_product_value(self.inventory,"Camera"), "The total value of Camera is: 5000.0 euros")
class TestProduct(unittest.TestCase):
    def test_create_product(self):
        # Vegetable object instance
        self.carrot = Vegetable.create_product(name="Carrot", price=1.50, quantity=100, expiry_date="12/2025")
        self.assertEqual(self.carrot.to_dict(), {'name': "Carrot", 'category': "Vegetable", 'price':1.50, 'quantity': 100, 'expiry_date': "12/2025" })
        
        # Fruit object instance
        self.apple = Fruit.create_product(name="Apple", price=0.30, quantity=150, season="Autumn")
        self.assertEqual(self.apple.to_dict(), {'name': "Apple", 'category': "Fruit", 'price':0.30, 'quantity': 150, 'season': "Autumn" })

        # Electronic object instance
        self.laptop = Electronic.create_product(name="Laptop", price=999.99, quantity=10, brand="HP", warranty_period=24)
        self.assertEqual(self.laptop.to_dict(), {'name': "Laptop", 'category': "Electronic", 'price':999.99, 'quantity': 10, 'brand': "HP", 'warranty_period': 24 })



if __name__ == "__main__":
    unittest.main()