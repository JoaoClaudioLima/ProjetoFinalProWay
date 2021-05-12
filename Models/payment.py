
class Payment:

    def __init__(self, payment_data: dict):
        self.total = payment_data['total']
        self.method = payment_data['method']
