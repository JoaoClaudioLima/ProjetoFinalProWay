from unittest import TestCase

from Utils.Process_order.validate_date import validate_date


class TestValidateDate(TestCase):

    def test_get_product(self):
        initial_date, final_date  = validate_date("2000-01-01", "2021-05-24")
        self.assertEqual(str(initial_date), "2000-01-01 00:00:00")
        self.assertEqual(str(final_date), "2021-05-24 00:00:00")

        initial_date, final_date = validate_date(None, None)
        self.assertEqual(str(initial_date), "2000-01-01 00:00:00")
        self.assertEqual(str(final_date), "2021-05-24 00:00:00")

