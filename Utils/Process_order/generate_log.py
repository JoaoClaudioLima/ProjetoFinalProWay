from datetime import datetime
from Controller.log_orders import LogOrders
from bson import ObjectId


class GenerateLog:
    date_time_at = datetime.today()

    def generate_log(self, user_id: str) -> str:
        log_order = dict(user_id=user_id, created_at=self.date_time_at)
        result = LogOrders().insert_log(log_order)
        return result

    def update_log(self, id_order: ObjectId, order_error: dict) -> dict:
        order_error.update(dict(updated_at=self.date_time_at))
        result = LogOrders().update_log(order_error, id_order)
        return result

    @staticmethod
    def get_log():
        result = LogOrders().get_log()
        return result


g = GenerateLog()
g.generate_log("12")
