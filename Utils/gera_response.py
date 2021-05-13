from flask import Response
import json


def gera_response(status, nome_conteudo, conteudo, mensagem=None):
    """
    Exemplos:
    1# return gera_response(200, "cadastro-provas", dict_values, "ok")
    2# return gera_response(400, "cadastro-provas", {}, "chave inválida")

    :param status: HTTP Status
    :param nome_conteudo: nome do conteudo
    :param conteudo: dicionario com dados
    :param mensagem: "ok", "erro..."
    :return: json com tudo.
    """
    body = {nome_conteudo: conteudo}
    if mensagem:
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")
