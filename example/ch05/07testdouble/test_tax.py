import io
import unittest
from unittest import mock
from tax import add_sales_tax


class SalesTaxTestCase(unittest.TestCase):
    @mock.patch('tax.urlopen')  # デコレータmock.patchが指定オブジェクトあるいはメソッドを真似る
    def test_get_sales_tax_returns_proper_value_from_api(
        self,
        mock_urlopen   # テスト関数がモックされたオブジェクトあるいはメソッドを受け取る
    ):
        test_tax_rate = 1.06
        mock_urlopen.return_value = io.BytesIO(  # モックされたurlopenの呼び出しが、モックされた応答（テスト用の税率）を返す
            str(test_tax_rate).encode('utf-8')
        )

        self.assertEqual(  # add_sales_taxがAPIから返された税率から新しい値を計算すると仮定してアサーションを作る
            5 * test_tax_rate,
            add_sales_tax(5, 'USA', 'MI')
        )
