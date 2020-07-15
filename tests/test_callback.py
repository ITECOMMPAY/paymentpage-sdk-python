
from payment_page_sdk.signature_handler import SignatureHandler
from payment_page_sdk.callback import Callback
from payment_page_sdk.process_exception import ProcessException
import json
import unittest


class CallbackTest(unittest.TestCase):
    secret = 'qwerty'
    payment_data =\
        {
            "payment":
                {
                    "id": "test-payment",
                    "status": "success"
                },
            "signature": "UGzKT0NC26f4u0niyJSQPx5q3kFFIndwLXeJVXahfCFwbY+Svg1WoXIxzrIyyjWUSLFhT8wAQ5SfBDRHnwm6Yg=="
        }
    payment_data_recursive =\
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
            "payment":
                {
                    "id": "test-payment"
                },
            "signature": "UGzKT0NC26f4u0niyJSQPx5q3kFFIndwLXeJVXahfCFwbYg34h32gh3"
        }
    payment_data_without_sign =\
        {
            "payment":
                {
                    "id": "test-payment"
                }
        }
    cb_data_without_payment =\
        {
            "project_id": "123",
            "recurring":
                {
                    "id": 321,
                    "status": "active",
                    "type": "Y",
                    "currency": "EUR",
                    "exp_year": "2025",
                    "exp_month": "12",
                    "period": "D",
                    "time": "11",
                },
            "signature": "AThqkBCZ6WZtY3WrMV28o7SM/vq6OIVF9qiVbELN4e/Ux59Lb5LFFnEuTq6bHa5pRvaPIkQGABXdpIrNLaeJdQ=="
        }

    @classmethod
    def setUp(cls):
        signature_handler = SignatureHandler(cls.secret)
        payment_data_raw = json.dumps(cls.payment_data)
        cls.callback = Callback(payment_data_raw, signature_handler)

    def test_get_payment(self):
        self.assertEqual(self.callback.get_payment(), self.payment_data['payment'])

    def test_get_payment_status(self):
        self.assertEqual(self.callback.get_payment_status(), self.payment_data['payment']['status'])

    def test_get_payment_id(self):
        self.assertEqual(self.callback.get_payment_id(), self.payment_data['payment']['id'])

    def test_get_signature(self):
        self.assertEqual(self.callback.get_signature(), self.payment_data['signature'])

    def test_decode_response(self):
        with self.assertRaises(ProcessException):
            self.callback.decode_response(json.dumps(self.payment_data)+'1')

    def test_recursive_get(self):
        with self.assertRaises(ProcessException):
            Callback(json.dumps(self.payment_data_recursive), SignatureHandler(self.secret))

    def test_invalid_signature(self):
        with self.assertRaises(ProcessException):
            signature_handler = SignatureHandler(self.secret)
            payment_data_raw = json.dumps(self.payment_data_invalid_signature)
            Callback(payment_data_raw, signature_handler)

    def test_get_null_param(self):
        signature_handler = SignatureHandler(self.secret)
        payment_data_raw = json.dumps(self.cb_data_without_payment)
        callback = Callback(payment_data_raw, signature_handler)
        self.assertEqual(callback.get_payment_status(), None)

    def test_undefined_sign(self):
        with self.assertRaises(ProcessException):
            signature_handler = SignatureHandler(self.secret)
            payment_data_raw = json.dumps(self.payment_data_without_sign)
            Callback(payment_data_raw, signature_handler)
