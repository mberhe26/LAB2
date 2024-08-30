# Mastewal Berhe, Sumeyya Sherief, & Rebecca Rogovich

import unittest
from shop import Shop
from customer import Customer



class Testcustomer(unittest.TestCase):
    def test_add_to_cart(self):
        
        customer_obj = Customer("May")
          
        customer_obj.add_item_to_inventory("Shoes", 10)  
        self.assertEqual(customer_obj.add_to_cart("Shoes", 5), "item added to cart")

    def test_decrease_item_quantity(self):
        shop_obj = Shop()
        shop_obj.add_item_to_inventory("Shoes", 10)

        self.assertTrue(shop_obj.decrease_item_quantity("Shoes", 5)) 
        self.assertEqual(shop_obj.inventory["Shoes"], 5)

        self.assertFalse(shop_obj.decrease_item_quantity("Shoes", 10)) 
        self.assertEqual(shop_obj.inventory["Shoes"], 5)
        


if __name__ == '__main__':
    unittest.main()
