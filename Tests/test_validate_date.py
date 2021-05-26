import datetime
from unittest import TestCase

from Utils.Process_order.validate_date import validate_date


class TestValidateDate(TestCase):

    def test_get_product(self):
        to_day = str(datetime.date.today())

        initial_date, final_date = validate_date("2000-01-01", to_day)
        self.assertEqual(str(initial_date), "2000-01-01 00:00:00.621017")
        self.assertEqual(str(final_date), f"{to_day} 23:59:59.999999")

        initial_date, final_date = validate_date(None, None)
        self.assertEqual(str(initial_date), "2000-01-01 08:36:39.621017")
        self.assertEqual(str(final_date), str(datetime.datetime.today()))


