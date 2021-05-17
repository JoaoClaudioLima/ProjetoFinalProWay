from flask_restful import Resource
from flask import request
from Utils.shipment.calculate_shipment import calculate_shipment_value
from Utils.gera_response import gera_response

ROUTE_KEY = "85906256179484450164927311732859959817"


class Shipment(Resource):
    """
    This Route receives the user info and returns the value of the shipment
    """

    @staticmethod
    def post():
        address = {"user": {"address": {}}}
        address['user']['address'] = request.json['address']
        header = dict(request.headers)
        try:
            if header['Key'] != ROUTE_KEY:
                return gera_response(400, "shipping", address, "invalid api-key")
        except KeyError:
            return gera_response(500, "shipping", address, "internal server error")

        try:
            address['shipping_price'] = calculate_shipment_value(address=address)
        except KeyError:
            return gera_response(400, "shipping", address, "address-state not informed.")

        if address['shipping_price'] is None:
            return gera_response(400, "shipping", address, "invalid address.")

        return gera_response(200, "shipping", address, "ok")
