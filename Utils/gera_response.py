from flask import Response
import json


def gera_response(status, content_index: str, content: dict, message=None):
    """
    Function that generate a flask Response with status, a body json

    :param status: HTTP Status
    :param content_index: content name
    :param content: dict with data
    :param message: "ok", "error..."
    :return: flask Response
    """

    body = {content_index: content}
    if message:
        body["log_message"] = message

    return Response(json.dumps(body), status=status, mimetype="application/json")
