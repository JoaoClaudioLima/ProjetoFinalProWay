import datetime
import uuid

BANK_NUMBER = "237"


def generate_bill(payment_data: dict) -> dict:
    """
    Function that generate a bill code with the bank number, datetime and uuid returns a dict.

    :param payment_data: dict with payment value.
    :return: returns a dict with due_date, documment_date, value and barcode.
    """

    bill = {'due_date': str(datetime.date.today() + datetime.timedelta(days=3)),
            'documment_date': str(datetime.date.today()), 'value': payment_data['total'],
            'barcode': f"{BANK_NUMBER}00.99999 {datetime.datetime.now().strftime('%m%d%Y.%H%M%S')} {str(uuid.uuid4().int).replace('-', '')}"}

    return bill
