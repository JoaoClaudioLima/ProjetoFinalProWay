from flask_restful import Resource
from flask import request
from Utils.payments.calculate_total import calculate_total
from Utils.gera_response import gera_response
from Utils.payments.validate_card import card_validating, confirm_payment


class Payment(Resource):
    @staticmethod
    def post():
        pay_info = request.json['payment']

        pay_info['total'] = calculate_total(items=pay_info['products'], shipping_price=pay_info['shipping_price'])

        try:
            if pay_info['method'] == 'credit':
                card_validation = card_validating(pay_info['card'])

                if card_validation['status']:
                    pay = confirm_payment(informed_card=pay_info['card'], method='credit', value=pay_info['total'])
                    if pay['status']:
                        pass
                    else:
                        return gera_response(400, "payment", pay_info, pay['message'])
                else:
                    return gera_response(400, "payment", pay_info, card_validation['message'])
            elif pay_info['method'] == 'debit':
                card_validation = card_validating(pay_info['card'])

                if card_validation['status']:
                    pay = confirm_payment(informed_card=pay_info['card'], method='debit', value=pay_info['total'])
                    if pay['status']:
                        pass
                    else:
                        return gera_response(400, "payment", pay_info, pay['message'])
                else:
                    return gera_response(400, "payment", pay_info, card_validation['message'])
            elif pay_info['method'] == 'bill':
                pass
            else:
                return gera_response(400, "payment", pay_info, "invalid pay method.")
        except KeyError:
            return gera_response(400, "payment", pay_info, "pay method not informed.")

        return gera_response(200, "payment", pay_info, "ok")
