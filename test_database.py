import unittest
import os
from database_module import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database(':memory:')  # Using in-memory database for testing
        self.sample_data = ('P001', 'Product1', 'User1', 'Address1', 'signature1', '2024-07-26 12:00:00')

    def test_insert_product(self):
        self.db.insert_product(*self.sample_data)
        product = self.db.fetch_product_by_pid('P001')
        self.assertIsNotNone(product)
        self.assertEqual(product[1], 'P001')

    def test_fetch_product_by_pid(self):
        self.db.insert_product(*self.sample_data)
        product = self.db.fetch_product_by_pid('P001')
        self.assertIsNotNone(product)
        self.assertEqual(product[1], 'P001')

    def test_fetch_all_products(self):
        self.db.insert_product(*self.sample_data)
        products = self.db.fetch_all_products()
        self.assertGreaterEqual(len(products), 1)

if __name__ == '__main__':
    unittest.main()
