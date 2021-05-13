

def calculate_total(items: list, shipping_price: float) -> float:
    """
    calculates the total of the cart
    :param items: list of itens
    :param shipping_price: price
    :return: total price of the cart
    """
    total = 0

    for item in items:
        total += item['item_price'] * item['item_quantity']

    if total > 0:
        total += shipping_price

    return total
