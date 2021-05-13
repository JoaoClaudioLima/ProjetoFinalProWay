from flask import Response
import json


def gera_response(status, content_index: str, content: dict, message=None):
    """
    Exemplos:
    1# return gera_response(200, "cadastro-provas", dict_values, "ok")
    2# return gera_response(400, "cadastro-provas", {}, "chave inválida")

    :param status: HTTP Status
    :param content_index: nome do conteudo
    :param content: dicionario com dados
    :param message: "ok", "erro..."
    :return: json com tudo.
    """
    body = {content_index: content}
    if message:
        body["message"] = message

    return Response(json.dumps(body), status=status, mimetype="application/json")
