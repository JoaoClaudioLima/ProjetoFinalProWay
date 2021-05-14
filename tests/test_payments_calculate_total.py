from unittest import TestCase
from Utils.payments.calculate_total import calculate_total


class TestCalculateTotal(TestCase):

    def test_calculate_total_works(self):
        items = [dict(item_price=0, item_quantity=1)]
        shipping_price = 10
        self.assertEqual(0, calculate_total(items=items, shipping_price=shipping_price))

        items.clear()
        items = [dict(item_price=10, item_quantity=1)]
        self.assertEqual(20, calculate_total(items=items, shipping_price=shipping_price))
