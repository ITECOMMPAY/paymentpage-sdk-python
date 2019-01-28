
from payment_page_sdk.SignatureHandler import SignatureHandler
import copy
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
                "signature": "UGzKT0NC26f4u0niyJSQPx5q3kFFIndwLXeJVXahfCFwbY+Svg1WoXIxzrIyyjWUSLFhT8wAQ5SfBDRHnwm6Yg=="
            }
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
