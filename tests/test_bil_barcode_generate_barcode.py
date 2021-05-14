from unittest import TestCase
from Utils.bil_barcode.generate_barcode import generate_barcode


class TestBilBarcode(TestCase):

    def test_generate_barcode_works(self):
        self.assertIsNone(generate_barcode("abc"))
