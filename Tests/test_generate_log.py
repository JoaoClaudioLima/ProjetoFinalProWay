from unittest import mock, TestCase
from Utils.Process_order.generate_log import GenerateLog


class TestOrder(TestCase):

    def test_generate_log(self):
        with mock.patch("Utils.Process_order.generate_log.LogOrders", create=True) as mock_log_orders:
            mock_log_orders().post.return_value = dict(status=True, message="OK", id_order="123")
            id_order = GenerateLog().generate_log("")
            self.assertEqual(id_order, dict(status=True, message="OK", id_order="123"))


    def test_update_log(self):
        with mock.patch("Utils.Process_order.generate_log.LogOrders", create=True) as mock_log_orders:
            mock_log_orders().put.return_value = dict(status=True, message="OK", id_order="123")
            id_order = GenerateLog().update_log("", "")
            self.assertEqual(id_order, dict(status=True, message="OK", id_order="123"))

    def test_get_log(self):
        with mock.patch("Utils.Process_order.generate_log.LogOrders", create=True) as mock_log_orders:
            mock_log_orders().get.return_value = dict(order=dict(products = [dict(name="Livro", price=25.50)]), message="OK", created_at="12/05/2021")
            order = GenerateLog().get_log()
            self.assertEqual(order, dict(order=dict(products = [dict(name="Livro", price=25.50)]), message="OK", created_at="12/05/2021"))
