from flask_restful import Api
from Controller.health_check import HealthCheck
from Controller.payment import Payment


def init_api(app):
    api = Api()

    api.add_resource(HealthCheck, "/health-check")
    api.add_resource(Payment, "/payment")

    api.init_app(app)
