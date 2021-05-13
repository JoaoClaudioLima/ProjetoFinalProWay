from flask import Response
import json


def gera_response(status, content_index: str, content: dict, message=None):
    """
    Exemplos:
    1# return gera_response(200, "user", dict_values, "ok")
    2# return gera_response(400, "users", {}, "invalid key")

    :param status: HTTP Status
    :param content_index: content name
    :param content: dict with data
    :param message: "ok", "error..."
    :return: Response
    """
    body = {content_index: content}
    if message:
        body["message"] = message

    return Response(json.dumps(body), status=status, mimetype="application/json")
