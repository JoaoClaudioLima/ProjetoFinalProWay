from flask_restful import Api
from Controller.health_check import HealthCheck
from Controller.payment import Payment


def init_api(app):
    """
    Function that executes on the initiation of the API and
    connect the controller classes with the respective routes.

    :param app: main app
    :return: API initialization
    """
    api = Api()

    api.add_resource(HealthCheck, "/health-check")
    api.add_resource(Payment, "/checkout")

    api.init_app(app)
