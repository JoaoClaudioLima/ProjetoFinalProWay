import pycard


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
