from datetime import datetime
from Controller.log_orders import LogOrders
from bson import ObjectId


class GenerateLog:
    date_time_at = datetime.today()

    def generate_log(self, order: dict) -> str:
        """
        The method creates a log with USER's Order data to be inserted into a LOG.
        The LOG is a table in our database.
        :param user_id: ID from the USER required to get its orders.
        :return: Returns the data inserted into the LOG.
        """

        log_order = dict(order=order, created_at=self.date_time_at)
        result = LogOrders().post(log_order=log_order)
        return result

    def update_log(self, id_order: ObjectId, order: dict) -> dict:
        """
        The method updates the log with the moment of any action performed by the USER.
        :return: Returns the data updated intorors that has occured during the process.
        :param id_order: The ID from the stated Order.
        :param order: The Code and Messa the LOG
        """
        result = LogOrders().put(log=order, id_order=id_order, updated_at=str(self.date_time_at))
        return result

    @staticmethod
    def get_log():
        """
        The method sends the entire LOG from the database.
        :return:
        """
        result = LogOrders().get()
        return result
