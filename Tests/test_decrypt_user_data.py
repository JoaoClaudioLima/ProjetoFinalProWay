from unittest import mock, TestCase
from Utils.decrypt_user_data import decrypt_user_data


class TestDecryptUserData(TestCase):

    @mock.patch("Utils.decrypt_user_data.Fernet")
    @mock.patch("Utils.decrypt_user_data.requests.get")
    def test_decrypt_data_works(self, mock_get, mock_fernet):
        mock_get().json.return_value = dict(_id="60a698046b43b955b9b875b5",
                                            email="pedrinho@gmail.com",
                                            cpf="gAAAAABgppgE5DhLjjNdY0E_aWaGC8cuGaDBYrEc9Or3EuJ8Qim8e94X681W09oeFyx0H0fd8l78ttZmnL_0z4iOFb9A_53p3g==",
                                            created_at="Thu, 20 May 2021 14:10:28 GMT",
                                            uploaded_at="Thu, 20 May 2021 14:10:28 GMT",
                                            first_name="gAAAAABgppgE6uwh38jLP2rrl7pjEZ5PTmj-zUHmFfNjSPMqS7vB6bdSL6e2lejfb5ptWPwVLt5hJdUClvRo5K7io3VxQPIT_w==",
                                            last_name="gAAAAABgppgEabrhrOue6r_-vL4mCmPDe1aBea_eeZq_RrVjM8fmGHGMorudP61DYTti-crUBbDbnKaQBB_o6V1-or_LV2pELA=="
                                            )
        actual_result = dict(_id="60a698046b43b955b9b875b5",
                             email="pedrinho@gmail.com",
                             cpf="10215436258",
                             created_at="Thu, 20 May 2021 14:10:28 GMT",
                             uploaded_at="Thu, 20 May 2021 14:10:28 GMT",
                             first_name="Pedro",
                             last_name="Lele"
                             )

        mock_fernet().decrypt().decode.side_effect = ["10215436258", "Pedro", "Lele"]
        self.assertEqual(decrypt_user_data("60a698046b43b955b9b875b5"), actual_result)

        mock_fernet().decrypt().decode.side_effect = ["16219836258", "Carlos", "Menez"]
        self.assertNotEqual(decrypt_user_data("60a698046b43b955b9b875b5"), actual_result)
