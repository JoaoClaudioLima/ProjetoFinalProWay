import json
import datetime
import uuid

BANK_NUMBER = "237"


def generate_bill(payment_data: dict) -> dict:
    bill = {}
    bill['due_date'] = datetime.date.today() + datetime.timedelta(days=3)
    bill['documment_date'] = datetime.date.today()
    bill['value'] = payment_data['total']
    bill['barcode'] = f"{BANK_NUMBER}00.10000 {str(uuid.uuid4()).replace('-', '')}.00000"
    return bill

print(generate_bill({"total": 34.5}))