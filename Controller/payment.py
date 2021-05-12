from flask_restful import Resource
from flask import Flask, jsonify, request
from Utils.calculate_total import calculate_total


class Payment(Resource):
    @staticmethod
    def post():
        pay_info = request.json['payment']

        total = calculate_total(items=pay_info['products'], shipping_price=pay_info['shipping_price'])

        print(total)
        return 200