from unittest import mock, TestCase
from Utils.py_fiscal.receipt import receipt_generator


class TestReceipt(TestCase):

    @mock.patch("Utils.py_fiscal.receipt.submit_email")
    @mock.patch("Utils.py_fiscal.receipt.SimpleInvoice")
    @mock.patch("Utils.py_fiscal.receipt.os")
    @mock.patch("Utils.py_fiscal.receipt.decrypt_user_data")
    def test_receipt_works(self, mock_decrypt, mock_os, mock_simple, mock_email):
        mock_decrypt.return_value = dict(email="pedro@gmail.com", first_name="pedro", last_name="Lelo", cpf="1252142517")
        pay_info = {
                "products": [
                    {
                        "title": "Livro 1",
                        "item_price": 10,
                        "quantity_purchased": 1
                    },
                    {
                        "title": "Livro 2",
                        "item_price": 5,
                        "quantity_purchased": 2
                    }
                ],
                "user": {
                    "user_id": "60a698046b43b955b9b875b5",
                    "address": {
                        "address_street": "Rua 7 de Setembro",
                        "address_number": 666,
                        "address_neighbourhood": "Centro",
                        "address_postal_code": "888888",
                        "address_city": "Blumenau",
                        "address_state": "SC"
                    }
                },
                "method": "debit",
                "card": {
                    "number": "344604579207048",
                    "month": "05",
                    "year": "2021",
                    "cvc": 336
                },
                "shipping_price": 20.0
            }
        mock_os.mkdir().return_value = True
        mock_simple = mock.MagicMock()
        mock_simple.InvoiceInfo.return_value = True
        mock_email.return_value = True

        self.assertEqual(receipt_generator(pay_info, "123"), True)


