from flask_restful import Resource
from Models.logDb import LogConnectionMongo
from pandas import DataFrame
from bson import ObjectId


class LogOrders(Resource):

    @staticmethod
    def post(log_order: dict):
        """
        The method inserts the order data into our LOG.
        :param log_order: Order's data and its content.
        :return: Returns a Status, Message and the ID number of the ORDER.
        If the insertion fails the return is an Exception with status and path message.
        """
        try:
            id_order = LogConnectionMongo().log.insert_one(log_order).inserted_id
            return dict(status=True, message="OK", id_order=str(id_order))
        except Exception as Error:
            return dict(status=False, message=Error.args)

    @staticmethod
    def put(log: dict, id_order: ObjectId, updated_at: str):
        """
        The method updates the LOG in our database with the order data. Every action and any error is registered.
        :param log: It's the data from error messages and where it has stopped.
        :param id_order: The ID number from the Order.
        :param updated_at: update time
        :return: Returns the ID that has been updated.
        If the update fails the return is an Exception with status and path message.
        """
        try:
            id_order = LogConnectionMongo().log.update_one({"_id": id_order}, {"$set": {"order": log,
                                                                               "updated_at": updated_at}})
            return dict(id_order=str(id_order))
        except Exception as Error:
            return dict(status=False, message=Error.args)
