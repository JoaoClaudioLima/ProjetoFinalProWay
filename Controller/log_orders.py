from flask_restful import Resource
from Models.logDb import LogConnectionMongo
from pandas import DataFrame
from bson import ObjectId


class LogOrders(Resource):

    @staticmethod
    def post(log_order: dict):
        try:
            id_order = LogConnectionMongo().log.insert_one(log_order).inserted_id
            return dict(status=True, message="OK", id_order=str(id_order))
        except Exception as Error:
            return dict(status=False, message=Error.args)

    @staticmethod
    def get():
        try:
            df = DataFrame(LogConnectionMongo().log.find())
            df = df.astype(str)
            return df.to_json(orient="records")
        except Exception as Error:
            return dict(status=False, message=Error.args)

    @staticmethod
    def put(log_error: dict, id_order: ObjectId):
        try:
            id_order = LogConnectionMongo().log.update_one({"_id": id_order}, {"$set": log_error})
            return dict(id_order=str(id_order))
        except Exception as Error:
            return dict(status=False, message=Error.args)
