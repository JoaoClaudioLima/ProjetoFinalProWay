from unittest import mock, TestCase
from Utils.Process_order.check_product import CheckProduct
from Utils.Process_order.get_product import GetProduct
from Utils.Process_order.get_user import GetUser


class TestOrder(TestCase):

    def test_get_product(self):
        with mock.patch("Utils.Process_order.get_product.requests", create=True) as mock_request:
            mock_request.get.return_value = dict(nome="Livro", price=2.50, digital=True)
            product = GetProduct().get_product("")
            self.assertEqual(product, {'nome': 'Livro', 'price': 2.5, 'digital': True})

        with mock.patch("Utils.Process_order.get_product.requests", create=True) as mock_request:
            mock_request.get.return_value = False
            product = GetProduct().get_product("")
            self.assertEqual(product, {'message': ("'bool' object is not iterable",), 'status': False})

    def test_get_user(self):
        with mock.patch("Utils.Process_order.get_user.requests", create=True) as mock_get_user:
            mock_get_user.get.return_value = dict(user=1)
            user = GetUser().get_user("")
            self.assertEqual(user, {'user': 1})

        with mock.patch("Utils.Process_order.get_user.requests", create=True) as mock_get_user:
            mock_get_user.get.return_value = False
            user = GetUser().get_user("")
            self.assertEqual(user, {'error': ("'bool' object is not iterable",), 'message': '60 - Internal Server Error.', 'status': False})

    def test_ckeck_product(self):
        with mock.patch("Utils.Process_order.get_product.GetProduct.get_product", create=True) as mock_get_product:
            mock_get_product.return_value = dict(products=dict(estoque=True))
            products = CheckProduct().check_products()
            self.assertTrue(products["products"]["estoque"])

        with mock.patch("Utils.Process_order.get_product.GetProduct.get_product", create=True) as mock_get_product:
            mock_get_product.return_value = dict(products=dict(estoque=False))
            products = CheckProduct().check_products()
            self.assertEqual(products, {'status': False, 'message': 'Product out of stock.', 'products': {'estoque': False}})
