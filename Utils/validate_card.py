import pycard
import json


def card_validating(card_info: dict) -> dict:
    """
    function for validate the card

    :param card_info: dict
    :return: dict with card info, status and a message.
    """
    card = pycard.Card(number=card_info['number'],
                       month=card_info['month'],
                       year=card_info['year'],
                       cvc=card_info['cvc'])

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

    return dict(card=card_info, status=return_status, message=return_msg)


# # payment_info = dict(number='Abc+',
# payment_info = dict(number='5162920626931788',
# # payment_info = dict(number='0000920626931788',
#                  month=1,
#                  year=2029,
#                  cvc=123)
#
# valid = card_validating(card_info=payment_info)
#
# print(valid['status'])

def verify_card_with_bank(informed_card: dict) -> bool:
    with open("cards.json", "r") as read_file:
        data = json.load(read_file)

    for card in data['cards']:
        if card['number'] == informed_card['number'] and \
                card['month'] == informed_card['month'] and \
                card['year'] == informed_card['year'] and \
                card['cvc'] == informed_card['cvc']:
            return True
    return False


# print(verify_card_with_bank({
#     "_id": "10",
#     "number": "5162920626931789",
#     "month": "04",
#     "year": "2021",
#     "cvc": 336
# }))