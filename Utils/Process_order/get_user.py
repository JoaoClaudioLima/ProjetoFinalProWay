import requests


class GetUser:

    @staticmethod
    def get_user(user_id: dict) -> dict:

        user = requests.get('http://127.0.0.1:5000/read/', params=user_id)

        return dict(user)
