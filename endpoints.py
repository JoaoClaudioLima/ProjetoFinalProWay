from flask_restful import Api
from Controller.log_order_reports import LogOrdersReports
from Controller.payment import Payment
from Controller.shipment import Shipment


def init_api(app):
    api = Api()

    api.add_resource(Payment, "/checkout")
    api.add_resource(Shipment, "/shipment")
    api.add_resource(LogOrdersReports, "/orders/reports/<int:search_type>")

    api.init_app(app)
