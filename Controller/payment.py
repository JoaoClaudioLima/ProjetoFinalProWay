from flask_restful import Resource
from flask import Flask, jsonify, request
from Utils.calculate_total import calculate_total
from Models.payment import Payment
from Utils.gera_response import gera_response


class Payment(Resource):
    @staticmethod
    def post():
        pay_info = request.json['payment']

        pay_info['total'] = calculate_total(items=pay_info['products'], shipping_price=pay_info['shipping_price'])

        # current_payment = Payment(payment_data=pay_info)
        try:
            if pay_info['method'] == 'credit':
                pass
            elif pay_info['method'] == 'debit':
                pass
            elif pay_info['method'] == 'bill':
                pass
            else:
                return gera_response(400, "payment", pay_info, "invalid pay method.")
        except KeyError:
            return gera_response(400, "payment", pay_info, "pay method not informed.")

        return gera_response(200, "payment", pay_info, "ok")
