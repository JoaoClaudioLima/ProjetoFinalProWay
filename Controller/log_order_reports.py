from flask import request
from flask_restful import Resource
from Models.logDb import LogConnectionMongo
from bson.json_util import dumps
from Utils.gera_response import gera_response
from Utils.Process_order.validate_date import validate_date


LOG_GENERAL = 1
LOG_BY_DATE = 2
LOGS = [LOG_GENERAL, LOG_BY_DATE]

ROUTE_KEY = "eadc34b8d3d1463097e6df66dfabd462"

class LogOrdersReports(Resource):

    @staticmethod
    def post(search_type: int) -> dict:
        """
        The method searches the entire LOG in JSON format.
        search_type: int that represents a type of search
        :return: Returns a JSON with all LOG data.
        If the search fails the return is an Exception with status and path message.
        """
        header = dict(request.headers)
        try:
            if header['Key'] != ROUTE_KEY:
                return gera_response(400, "payment", "invalid api-key")
        except KeyError:
            return gera_response(500, "payment", "internal server error")

        request_body = request.get_json()
        result_list = []

        from_dt, to_dt = validate_date(initial_date=request_body["initial_date"],
                                       final_date=request_body["final_date"])

        if search_type not in LOGS:
            return gera_response(400, "orders", request_body, "invalid search type.")

        elif search_type == LOG_GENERAL:
            try:
                result_list = list(LogConnectionMongo().log.find({"created_at": {"$gte": from_dt, "$lte": to_dt}}))
            except Exception as Error:
                return gera_response(400, "orders", request_body, Error)

        elif search_type == LOG_BY_DATE:
            try:
                result_list = list(LogConnectionMongo().log.find({"$and": [{"created_at": {"$gte": from_dt, "$lte": to_dt}}, {"order.status": "paid"}]}))
                for i in result_list:
                    i['created_at'] = str(i['created_at'])
            except Exception as Error:
                return gera_response(400, "orders", request_body, Error)

        return gera_response(200, "orders", dumps(result_list, indent=2), "ok")
