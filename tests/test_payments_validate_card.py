from unittest import TestCase, mock
from Utils.payments.validate_card import *


class TestValidateCard(TestCase):

    def test_card_validating_works(self):
        test_card = dict(number="344604579207048",
                         month="05",
                         year="2021",
                         cvc=336)
        expected_return = {'message': 'Card is valid', 'status': True}
        self.assertEqual(expected_return, card_validating(card_info=test_card))

        test_card = dict(number="5344604579207048",
                         month="05",
                         year="2021",
                         cvc=336)
        expected_return = {'message': 'Card is not valid', 'status': False}
        self.assertEqual(expected_return, card_validating(card_info=test_card))

        test_card = dict(number="344604579207048",
                         month="04",
                         year="2021",
                         cvc=336)
        expected_return = {'message': 'Card is expired', 'status': False}
        self.assertEqual(expected_return, card_validating(card_info=test_card))

    def test_confirm_payment_works(self):
        read_file = json.dumps({
            "cards": [{"number": 55,
                      "month": "05",
                      "year": "2021",
                      "cvc": 336,
                      "credit_limit": 500,
                      "credit_used": 0,
                      "debit": 400},
                      {"number": 44,
                       "month": "04",
                       "year": "2021",
                       "cvc": 336,
                       "credit_limit": 500,
                       "credit_used": 0,
                       "debit": 400}]
        })

        mock_open = mock.mock_open(read_data=read_file)
        with mock.patch("Utils.payments.validate_card.open", mock_open):
            test_card = dict(number="344604579207048",
                             month="05",
                             year="2021",
                             cvc="336")
            expected_return = {'message': 'operation not allowed', 'status': False}
            self.assertEqual(expected_return, confirm_payment(informed_card=test_card,
                                                method='credit',
                                                value=999))

            test_card = dict(number="44",
                             month="04",
                             year="2021",
                             cvc="336")
            expected_return = 0
            self.assertEqual(expected_return, confirm_payment(informed_card=test_card,
                                                              method='credit',
                                                              value=1))
