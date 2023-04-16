import unittest

from cart import ShoppingCart
from product import Product


class ShoppingCartTestCase(unittest.TestCase):
    def test_add_and_remove_product(self):
        cart = ShoppingCart()  # カートを生成
        product = Product('shoes', 'S', 'blue')  # Sサイズの青の靴を生成

        cart.add_products(product)  # 靴をカートに追加
        cart.remove_product(product)  # カートから靴を削除

        self.assertDictEqual({}, cart.products)  # カートは空になっているはず

# cd example/ch05/06unittest5; python3 -m unittest
