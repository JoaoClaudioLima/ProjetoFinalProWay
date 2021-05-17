from flask_restful import Resource
from flask import request
from Utils.payments.calculate_total import calculate_total
from Utils.gera_response import gera_response
from Utils.payments.validate_card import card_validating, confirm_payment
from Utils.payments.bill_generator import generate_bill
from Utils.shipment.calculate_shipment import calculate_shipment_value


ROUTE_KEY = "228123976667561672010756977690311737153"

def card_payment(pay_info: dict):
    """
    Méthod that validates the card and does the debit/credit operation and returns a response

    :param pay_info: Data from the payment
    :return: Response
    """
    card_validation = card_validating(pay_info['card'])

    if not card_validation['status']:
        return gera_response(400, "payment", pay_info, card_validation['message'])

    pay = confirm_payment(informed_card=pay_info['card'], method=pay_info['method'], value=pay_info['total'])
    if pay['status']:
        pay_info['status'] = "paid"
        pass
    else:
        return gera_response(400, "payment", pay_info, pay['message'])


class Payment(Resource):
    """
    This Route checks the payment option and concludes the checkout process as a whole. Verifing if the operation is
    a valid one and generating the necessary logs.
    """

    @staticmethod
    def post():
        pay_info = request.json['checkout']

        header = dict(request.headers)
        try:
            if header['Key'] != ROUTE_KEY:
                return gera_response(400, "payment", pay_info, "invalid api-key")
        except KeyError:
            return gera_response(500, "payment", pay_info, "internal server error")
        
        pay_info['shipping_price'] = calculate_shipment_value(pay_info)
        
        pay_info['total'] = calculate_total(items=pay_info['products'], shipping_price=pay_info['shipping_price'])

        try:
            if pay_info['method'] not in ["credit", "debit", "bill"]:
                return gera_response(400, "payment", pay_info, "invalid pay method.")

            elif pay_info['method'] in ["credit", "debit"]:
                card_payment(pay_info=pay_info)

            elif pay_info['method'] == 'bill':
                pay_info['status'] = "waiting bill"
                pay_info['bill'] = generate_bill(payment_data=pay_info)

        except KeyError:
            return gera_response(400, "payment", pay_info, "pay method not informed.")

        return gera_response(200, "payment", pay_info, "ok")
