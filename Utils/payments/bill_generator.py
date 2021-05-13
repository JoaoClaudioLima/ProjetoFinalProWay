import datetime
import uuid

BANK_NUMBER = "237"


def generate_bill(payment_data: dict) -> dict:
    bill = {}
    bill['due_date'] = str(datetime.date.today() + datetime.timedelta(days=3))
    bill['documment_date'] = str(datetime.date.today())
    bill['value'] = payment_data['total']
    bill['barcode'] = f"{BANK_NUMBER}00.99999 {datetime.datetime.now().strftime('%m%d%Y.%H%M%S')} {str(uuid.uuid4().int).replace('-', '')}"

    return bill

# bil = generate_bill({"total": 34.5})
# print(bil)

