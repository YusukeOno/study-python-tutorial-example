import unittest

from product import Product


class ProductTestCase(unittest.TestCase):
    def test_trasform_name_for_sku(self):
        small_black_shoes = Product('shoes', 'S', 'black')
        expected_value = 'SHOES'
        actual_value = small_black_shoes.transform_name_for_sku()
        self.assertEqual(expected_value, actual_value)

# cd example/ch05/04unittest3; python3 -m unittest
