from flask_restful import Api
from Controller.health_check import HealthCheck


def init_api(app):
    api = Api()

    api.add_resource(HealthCheck, "/health-check")

    api.init_app(app)
