import json


def credit_payment(payment_data: dict):
    pass


def debit_payment(payment_data: dict):
    pass


def generate_bill(payment_data: dict):
    pass


def verify_card_with_bank(informed_card: dict) -> bool:
    with open("cards.json", "r") as read_file:
        data = json.load(read_file)

    for card in data['cards']:
        if card['number'] == informed_card['number'] and \
            card['month'] == informed_card['month'] and \
                card['year'] == informed_card['year'] and \
                    card['cvc'] == card['cvc']:
            return True
    return False


print(verify_card_with_bank({
    "_id": "10",
    "number": "5162920626931789",
    "month": "04",
    "year": "2021",
    "cvc": 336
}))