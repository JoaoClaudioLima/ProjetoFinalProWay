import pycard
import json


def card_validating(card_info: dict) -> dict:
    """
    function for validate the card

    :param card_info: dict
    :return: dict with status and a message.
    """
    card = pycard.Card(number=card_info['number'],
                       month=int(card_info['month']),
                       year=int(card_info['year']),
                       cvc=int(card_info['cvc']))

    if card.is_expired:
        return_status = False
        return_msg = "Card is expired"
    elif not card.is_mod10_valid:
        return_status = False
        return_msg = "Card is not valid"
    else:
        return_status = True
        return_msg = "Card is valid"

    card_info['brand'] = card.friendly_brand

    return dict(status=return_status, message=return_msg)


# # payment_info = dict(number='Abc+',
# payment_info = dict(number='344604579207048',
# # payment_info = dict(number='0000920626931788',
#                  month=5,
#                  year=2021,
#                  cvc=336)
#
# valid = card_validating(card_info=payment_info)
# print(valid)

def confirm_payment(informed_card: dict, method: str, value: float) -> dict:
    with open("Utils/payments/cards.json", "r") as read_file:
        data = json.load(read_file)

    for card in data['cards']:
        if card['number'] == informed_card['number'] and \
                card['month'] == informed_card['month'] and \
                card['year'] == informed_card['year'] and \
                card['cvc'] == informed_card['cvc']:
            if method == 'credit':
                if card['credit_used'] + value <= card['credit_limit']:
                    card['credit_used'] = card['credit_used'] + value
                else:
                    return dict(status=False, message="insufficient credit balance")
            elif method == 'debit':
                if card['debit'] >= value:
                    card['debit'] = card['debit'] - value
                else:
                    return dict(status=False, message="insufficient debit balance")

            with open('Utils/payments/cards.json', 'w') as outfile:
                json.dump(data, outfile)

            return dict(status=True, message="ok")

    return dict(status=False, message="operation not allowed")


# print(confirm_payment(informed_card={
#     "_id": "10",
#     "number": "344604579207048",
#     "month": "05",
#     "year": "2021",
#     "cvc": 336
# }, method='debit', value=1))