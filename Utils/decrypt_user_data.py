import requests
from cryptography.fernet import Fernet

key = b"K22eIoXBwOnMuJL6nRo0GOIZLGNgGa_diB_FJvUa3AY="


def decrypt_user_data(user_id: str) -> dict:
    """
    The function receive a user_id for search in user api the datas of user, decrypt this datas to use it
    on generate of user receipt
    :param user_id: The unique identification of each registered user
    :return data: The user datas decrypted
    """
    data = requests.get(f"http://192.168.0.74:5030/user/{user_id}",
                        headers=dict(Key="WADCAlhXPqJ4UL3JwO4fkhsAV8rIyE")).json()
    for d in data:
        if d not in ["_id", "created_at", "date_of_birth", "email", "uploaded_at"]:
            data[d] = Fernet(key).decrypt(data[d].encode()).decode()
    return data

