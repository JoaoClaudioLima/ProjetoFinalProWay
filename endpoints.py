from Controller.health_check import HealthCheck
from Controller.log_orders import LogOrders
from flask_restful import Api


def init_api(app):
    api = Api()

    api.add_resource(HealthCheck, "/health-check")
    api.add_resource(LogOrders, "/log-orders")

    api.init_app(app)
