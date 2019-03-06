
from payment_page_sdk.signature_handler import SignatureHandler
from payment_page_sdk.callback import Callback
from payment_page_sdk.process_exception import ProcessException
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
    payment_data_invalid_signature =\
        {
            "body": {
                "payment":
                    {
                        "id": "test-payment"
                    },
                "signature": "UGzKT0NC26f4u0niyJSQPx5q3kFFIndwLXeJVXahfCFwbYg34h32gh3"
            }
        }
    payment_data_without_status =\
        {
            "body": {
                "payment":
                    {
                        "id": "test-payment"
                    },
                "signature": "yVp+lFVggXb0iitKgb49yfl/riUGRXMaTVCqiJTEbfkIt2PCpIR3vwyBg+SgtsoG4HTDdg9X7rxi0A1R/U2O5w=="
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

    def test_invalid_signature(self):
        with self.assertRaises(ProcessException):
            signature_handler = SignatureHandler(self.secret)
            payment_data_raw = json.dumps(self.payment_data_invalid_signature)
            Callback(payment_data_raw, signature_handler)

    def test_get_null_param(self):
        signature_handler = SignatureHandler(self.secret)
        payment_data_raw = json.dumps(self.payment_data_without_status)
        callback = Callback(payment_data_raw, signature_handler)
        self.assertEqual(callback.get_payment_status(), None)
