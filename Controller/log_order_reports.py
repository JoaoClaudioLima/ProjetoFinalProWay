from flask import request
from flask_restful import Resource
from Models.logDb import LogConnectionMongo
from bson.json_util import dumps
from Utils.gera_response import gera_response
from Utils.Process_order.validate_date import validate_date


class LogOrdersReports(Resource):
    @staticmethod
    def post(search_type: int) -> dict:
        """
        The method searches the entire LOG in JSON format.
        search_type: int that represents a type of search
        :return: Returns a JSON with all LOG data.
        If the search fails the return is an Exception with status and path message.
        """
        request_body = request.get_json()
        result_list = []

        from_dt, to_dt = validate_date(initial_date=request_body["initial_date"],
                                       final_date=request_body["final_date"])

        if search_type not in [1, 2]:
            return gera_response(400, "orders", request_body, "invalid search type.")

        elif search_type == 1:
            try:
                result_list = list(LogConnectionMongo().log.find())
            except Exception as Error:
                return gera_response(400, "orders", request_body, Error)

        elif search_type == 2:
            try:
                result_list = list(LogConnectionMongo().log.find({"created_at": {"$gte": from_dt, "$lte": to_dt}}))
                for i in result_list:
                    i['created_at'] = str(i['created_at'])
            except Exception as Error:
                return gera_response(400, "orders", request_body, Error)

        return gera_response(200, "orders", dumps(result_list, indent=2), "ok")