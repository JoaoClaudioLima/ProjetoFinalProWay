from unittest import mock, TestCase
from Controller.log_orders import LogOrders

class TestLogOrder(TestCase):

    @mock.patch("Controller.log_orders.LogConnectionMongo")
    def test_post(self, mock_log_conn):
        mock_log_conn().log.insert_one().inserted_id = "123"

        result = LogOrders().post({})
        expected = dict(status=True, message="OK", id_order="123")
        self.assertEqual(result, expected)

        delattr(mock_log_conn(), "log")
        result2 = LogOrders().post({})
        expected2 = dict(status=False, message=("log",))
        self.assertEqual(result2, expected2)


    @mock.patch("Controller.log_orders.LogConnectionMongo")
    def test_put(self, mock_log_conn):
        mock_log_conn().log.update_one.return_value = "123"

        result = LogOrders().put({}, "", "")
        expected = dict(id_order="123")
        self.assertEqual(result, expected)

        delattr(mock_log_conn(), "log")
        result2 = LogOrders().put({}, "", "")
        expected2 = dict(status=False, message=("log",))
        self.assertEqual(result2, expected2)