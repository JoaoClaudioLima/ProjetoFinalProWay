from unittest import TestCase, mock
from Utils.shipment.calculate_shipment import calculate_shipment_value


class TestCalculateShipment(TestCase):

    def test_calculate_shipment_value_works(self):
        read_return = """{"RO": 50.0, "AC": 5000.0, "RM": 50.0}"""
        with mock.patch("Utils.shipment.calculate_shipment.open", mock.mock_open(read_data=read_return)):

            dic = dict(checkout=dict(user=dict(address=dict(address_state="RO"))))
            value = 50.0
            self.assertEqual(calculate_shipment_value(dic), value)

        with mock.patch("Utils.shipment.calculate_shipment.json") as mock_json:
            delattr(mock_json, "loads")
            self.assertEqual(calculate_shipment_value({}), "loads")
