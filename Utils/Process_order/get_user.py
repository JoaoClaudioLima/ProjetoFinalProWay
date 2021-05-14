import requests
from bson import ObjectId


class GetUser:

    def get_user(self, user_id: dict) -> dict:

        user = requests.get('http://127.0.0.1:5000/read/', params=user_id)

        print(user.text)
        # return user


g = GetUser()
g.get_user(dict(_id=ObjectId("609d1a1ebb16e5a3476fd09f")))
