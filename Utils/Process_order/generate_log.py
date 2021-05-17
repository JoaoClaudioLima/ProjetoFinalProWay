from datetime import datetime
from Controller.log_orders import LogOrders
from bson import ObjectId


class GenerateLog:
    date_time_at = datetime.today()

    def generate_log(self, user_id: str) -> str:
        """
        The method creates a log with USER's Order data to be inserted into a LOG.
        The LOG is a table in our database.
        :param user_id: ID from the USER required to get its orders.
        :return: Returns the data inserted into the LOG.
        """

        log_order = dict(user_id=user_id, created_at=self.date_time_at)
        result = LogOrders().post(log_order)
        return result

    def update_log(self, id_order: ObjectId, order_error: dict) -> dict:
        """
        The method updates the log with the moment of any action performed by the USER.
        The Update method will register the errors that has occured during the process.
        :param id_order: The ID from the stated Order.
        :param order_error: The Code and Message from the error.
        :return: Returns the data updated into the LOG
        """
        order_error.update(dict(updated_at=self.date_time_at))
        result = LogOrders().put(order_error, id_order)
        return result

    @staticmethod
    def get_log():
        """
        The method sends the entire LOG from the database.
        :return:
        """
        result = LogOrders().get()
        return result
