import json
from unittest import mock, TestCase
from Utils.SubmitEmail.submit_email import SubmitEmail


class TestSubmitEmail(TestCase):

    @mock.patch("Utils.SubmitEmail.submit_email.encoders")
    @mock.patch("Utils.SubmitEmail.submit_email.MIMEBase")
    @mock.patch("Utils.SubmitEmail.submit_email.MIMEMultipart")
    @mock.patch("Utils.SubmitEmail.submit_email.smtplib")
    def test_submit(self, mock_smt, mock_MINE, mock_MIMEBase, mock_encoders):
        read_file = json.dumps({
            "Nota": "Test" })

        mock_open = mock.mock_open(read_data=read_file)
        with mock.patch("main.open", mock_open):
            result = SubmitEmail().submit("")
            self.assertTrue(result)

        delattr(mock_smt.SMTP(), "login")
        result = SubmitEmail().submit("")
        self.assertEqual(result, {'status': False, 'message': ('login',)})