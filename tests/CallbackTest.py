
from payment_page_sdk.SignatureHandler import SignatureHandler
from payment_page_sdk.Callback import Callback
from payment_page_sdk.ProcessException import ProcessException
import json
import unittest


class CallbackTest(unittest.TestCase):
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
        signature_handler = SignatureHandler(cls.secret)
        payment_data_raw = json.dumps(cls.payment_data)
        cls.callback = Callback(payment_data_raw, signature_handler)

    def test_get_payment(self):
        self.assertEqual(self.callback.get_payment(), self.payment_data['body']['payment'])

    def test_get_payment_status(self):
        self.assertEqual(self.callback.get_payment_status(), self.payment_data['body']['payment']['status'])

    def test_get_payment_id(self):
        self.assertEqual(self.callback.get_payment_id(), self.payment_data['body']['payment']['id'])

    def test_get_signature(self):
        self.assertEqual(self.callback.get_signature(), self.payment_data['body']['signature'])

    def test_decode_response(self):
        with self.assertRaises(ProcessException):
            self.callback.decode_response(json.dumps(self.payment_data)+'1')
