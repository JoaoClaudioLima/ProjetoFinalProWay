import requests


class GetUser:

    def get_user(self, user_id: dict) -> dict:
        """
        The method makes a request from the User ID to the User API by the URL and gets user with its data.
        If the connection fails the method returns an error with a message.
        :param user_id: The ID from the USER.
        :return: A dictionary with the USER data.
        """

        try:
            user = requests.get('http://127.0.0.1:5000/read/', params=user_id)
            return dict(user)
        except Exception as Error:
            return dict(status=False, message="60 - Internal Server Error.", error=Error.args)
