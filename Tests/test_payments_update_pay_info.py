from unittest import TestCase, mock
from Utils.payments.update_pay_info import *


class TestUpdatePayInfo(TestCase):

    @mock.patch("Utils.payments.update_pay_info.ObjectId")
    @mock.patch("Utils.payments.update_pay_info.gera_response")
    @mock.patch("Utils.Process_order.generate_log.GenerateLog.update_log")
    @mock.patch("Utils.payments.update_pay_info.CheckProduct.check_products")
    @mock.patch("Utils.payments.update_pay_info.GetProduct.get_product")
    def test_update_pay_info_works(self, mock_get_product, mock_check_product, mock_generate_log, mock_gera_response, mock_ObjectId):
        mock_get_product.return_value = dict(books_stocks=[dict(title="test", item_price="test"),
                                                           dict(title="test", item_price="test"),
                                                           dict(title="test", item_price="test")],
                                             digital="test")
        mock_check_product.return_value = True
        expected_return = {'checkout': {'products': [{'item_price': 'test', 'test': 'test', 'title': 'test'},
                                                     {'item_price': 'test', 'test': 'test', 'title': 'test'},
                                                     {'item_price': 'test', 'test': 'test', 'title': 'test'}]},
                           'digital_books': 'test'}
        self.assertEqual(expected_return, update_pay_info(dict(checkout=dict(products=[dict(test="test"),
                                                                                       dict(test="test"),
                                                                                       dict(test="test")])),
                                                          dict(test="test")))

        mock_check_product.return_value = False
        mock_ObjectId.return_value = "test"
        mock_generate_log.return_value = "test"
        mock_gera_response.return_value = "test"
        self.assertEqual("test", update_pay_info(dict(checkout=dict(products=[dict(test="test"),
                                                                              dict(test="test"),
                                                                              dict(test="test")])),
                                                 dict(id_order="test")))
