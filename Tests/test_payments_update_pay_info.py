from unittest import TestCase, mock
from Utils.payments.update_pay_info import *


class TestUpdatePayInfo(TestCase):

    @mock.patch("Utils.payments.update_pay_info.CheckProduct.check_products")
    @mock.patch("Utils.payments.update_pay_info.GetProduct.get_product")
    def test_update_pay_info_works(self, mock_get_product, mock_check_product):
        mock_get_product.return_value = dict(books_stocks=[dict(title="test", item_price="test"),
                                                           dict(title="test", item_price="test"),
                                                           dict(title="test", item_price="test")],
                                             digital="test")
        mock_check_product.return_value = True
        expected_return = {'products': [{'item_price': 'test', 'test': 'test', 'title': 'test'},
                                                     {'item_price': 'test', 'test': 'test', 'title': 'test'},
                                                     {'item_price': 'test', 'test': 'test', 'title': 'test'}],
                           'digital_books': 'test'}
        self.assertEqual(expected_return, update_pay_info(dict(products=[dict(test="test"),
                                                                         dict(test="test"),
                                                                         dict(test="test")])))

        mock_check_product.return_value = False
        self.assertEqual(dict(products=[dict(test="test"),
                                                                dict(test="test"),
                                                                dict(test="test")],
                              message='products out of stock.'),
                         update_pay_info(dict(products=[dict(test="test"),
                                                                dict(test="test"),
                                                                dict(test="test")])))
