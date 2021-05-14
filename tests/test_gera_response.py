from unittest import TestCase
from Utils.gera_response import gera_response


class TestGenResponse(TestCase):

    def test_gera_response_works(self):
        self.assertEqual('<Response 13 bytes [200 OK]>', str(gera_response(200, 'title', {}, None)))

        self.assertEqual('<Response 29 bytes [400 BAD REQUEST]>', str(gera_response(400, 'title', {}, 'a')))
