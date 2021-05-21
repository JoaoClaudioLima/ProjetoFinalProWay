from Controller.health_check import HealthCheck
from flask_restful import Api
from Controller.payment import Payment
from Controller.shipment import Shipment
from Utils.Process_order.generate_log import GetLog


def init_api(app):
    """
    Function that executes on the initiation of the API and
    connect the controller classes with the respective routes.
    :param app: main app
    :return: API initialization
    """
    api = Api()

    api.add_resource(HealthCheck, "/health-check")
    api.add_resource(GetLog, "/log-orders")
    api.add_resource(Payment, "/checkout")
    api.add_resource(Shipment, "/shipment")

    api.init_app(app)