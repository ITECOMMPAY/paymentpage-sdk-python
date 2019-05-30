
from payment_page_sdk.signature_handler import SignatureHandler
from payment_page_sdk.callback import Callback
import copy
import json
import unittest


class SignatureHandlerTest(unittest.TestCase):
    secret = 'qwerty'
    payment_data =\
        {
            "body": {
                "payment":
                    {
                        "id": "test-payment",
                        "status": "success"
                    },
                "some_bool_param": True,
                "signature": "TZS0J65ReNUMgKzeXUey9xOGGyC7r4OhsFXt/3H8XZM2Le8Wot2E1NIjeSPOyV1F3sUU6F3kfo9om2dhbe3ieA=="
            }
        }
    payment_multilevel_data =\
        {
            "payment":
                {
                    "id": "test-payment"
                },
            "errors":
                [
                    {
                        "code": "123",
                        "message": "grand crash",
                        "description": [
                            "description-str",
                            {
                                "description1": 1
                            }
                        ]
                    },
                    {
                        "code": "456",
                        "message": "minor crash"
                    }
                ],
            "signature": "i6F9q/cfj8T+r/9z1U1f+WgGe0Y/2L2Ml7pp6x6GKLmS0SwbEzcD1/DJ2Hx4PwSgyD696SU19MjtHBF0gv+LKA=="
        }

    @classmethod
    def setUp(cls):
        cls.signature_handler = SignatureHandler(cls.secret)

    def test_check(self):
        compare_data = copy.deepcopy(self.payment_data)
        signature = compare_data['body']['signature']
        del compare_data['body']['signature']
        self.assertTrue(self.signature_handler.check(compare_data['body'], signature))

    def test_sign(self):
        compare_data = copy.deepcopy(self.payment_data)
        del compare_data['body']['signature']
        self.assertEqual(
            self.payment_data['body']['signature'],
            self.signature_handler.sign(compare_data['body'])
        )

    def test_multilevel_callback(self):
        signature_handler = SignatureHandler(self.secret)
        payment_data_raw = json.dumps(self.payment_multilevel_data)
        Callback(payment_data_raw, signature_handler)
