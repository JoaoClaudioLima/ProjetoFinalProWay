import json


def calculate_shipments(address: dict) -> float:
    """
    Calculate shipment based on JSON file
    :param address: same format as "Info/retorno_front_cartoes.json"
    :return: float
    """

    try:
        with open("Utils/shipment/shipping_prices.json", "r") as read_file:
            data = json.loads(read_file.read())
    except Exception as error:
        return error.args[0]
    for state in data:
        if state == address['address_state']:
            shipping_value = data[state]
            return shipping_value
