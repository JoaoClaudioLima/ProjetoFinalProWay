from unittest import TestCase
from Utils.payments.bill_generator import generate_bill


class TestBilGenerator(TestCase):

    def test_generate_bill_works(self):
        self.assertEqual(dict, type(generate_bill(dict(total=30))))
