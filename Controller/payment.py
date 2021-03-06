from bson import ObjectId
from flask_restful import Resource
from flask import request
from Utils.payments.calculate_total import calculate_total
from Utils.gera_response import gera_response
from Utils.payments.validate_card import card_validating, confirm_payment
from Utils.payments.bill_generator import generate_bill
from Utils.shipment.calculate_shipment import calculate_shipment_value
from Utils.Process_order.generate_log import GenerateLog
from Utils.payments.update_pay_info import update_pay_info
from Utils.Process_order.get_product import GetProduct
from Utils.py_fiscal.receipt import receipt_generator


ROUTE_KEY = "228123976667561672010756977690311737153"


def card_payment(log_order: dict, pay_info: dict):
    """
    Method that validates the card and does the debit/credit operation and returns a response

    :param pay_info: Data from the payment
    :param log_order: Dict with database order info
    :return: Response
    """
    card_validation = card_validating(pay_info['card'])
    log = GenerateLog()

    if not card_validation['status']:
        pay_info['message'] = card_validation['message']
        pay_info['status'] = "not paid"
        GetProduct().post_response(pay_info["products"], False)
        log.update_log(id_order=ObjectId(log_order['id_order']), order=pay_info)
        return gera_response(400, "payment", pay_info, pay_info['message'])

    pay = confirm_payment(informed_card=pay_info['card'], method=pay_info['method'], value=pay_info['total'])
    if pay['status']:
        pay_info['status'] = "paid"
        pay_info['message'] = "ok"
        pass
    else:
        pay_info['status'] = "not paid"
        pay_info['message'] = pay['message']
        GetProduct().post_response(pay_info["products"], False)
        log.update_log(id_order=ObjectId(log_order['id_order']), order=pay_info)
        return gera_response(400, "payment", pay_info, pay_info['message'])


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

        log = GenerateLog()
        log_order = log.generate_log(order=pay_info)

        if log_order['status'] is False:
            pay_info['message'] = log_order['message']
            gera_response(500, "payment", pay_info, pay_info['message'])

        pay_info = update_pay_info(pay_info)
        if 'message' in pay_info.keys():
            if pay_info['message'] == "products out of stock.":
                GenerateLog().update_log(id_order=ObjectId(log_order['id_order']), order=pay_info)
                return gera_response(400, "payment", pay_info, pay_info['message'])

        pay_info['shipping_price'] = 0.0 if pay_info['digital_books'] else calculate_shipment_value(pay_info)

        pay_info['total'] = calculate_total(items=pay_info['products'], shipping_price=pay_info['shipping_price'])
        try:
            if pay_info['method'] not in ["credit", "debit", "bill"]:
                pay_info['message'] = "invalid pay method."
                GetProduct().post_response(pay_info["products"], False)
                log.update_log(id_order=ObjectId(log_order['id_order']), order=pay_info)
                return gera_response(400, "payment", pay_info, pay_info['message'])

            elif pay_info['method'] in ["credit", "debit"]:
                card_payment(log_order=log_order, pay_info=pay_info)

            elif pay_info['method'] == 'bill':
                pay_info['status'] = "waiting bill"
                pay_info['bill'] = generate_bill(payment_data=pay_info)
                pay_info['message'] = "ok"
                log.update_log(id_order=ObjectId(log_order['id_order']), order=pay_info)
                return gera_response(200, "payment", pay_info, pay_info['message'])
        except KeyError:
            pay_info['message'] = "pay method not informed."
            GetProduct().post_response(pay_info["products"], False)
            log.update_log(id_order=ObjectId(log_order['id_order']), order=pay_info)
            return gera_response(400, "payment", pay_info, pay_info['message'])
        receipt_generator(pay_info, log_order["id_order"])
        GetProduct().post_response(pay_info["products"], True)
        log.update_log(id_order=ObjectId(log_order['id_order']), order=pay_info)
        return gera_response(200, "payment", pay_info, pay_info['message'])
