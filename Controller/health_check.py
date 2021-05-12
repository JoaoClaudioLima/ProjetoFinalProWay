from flask_restful import Resource


class HealthCheck(Resource):
    @staticmethod
    def get():
        return 'ok', 200