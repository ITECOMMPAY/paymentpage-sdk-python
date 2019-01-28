
from payment_page_sdk.Gate import Gate
from payment_page_sdk.Payment import Payment
from datetime import datetime
from urllib import parse as urlparse
from payment_page_sdk.Callback import Callback
import json
import unittest


class GateTest(unittest.TestCase):
    secret = 'qwerty'
    compare_url = \
        'https://paymentpage.ecommpay.com/payment?payment_id=test-payment&cashier_predefined_amounts=1%2C2%2C3' \
        + '&project_id=1&best_before=2055-05-05T00%3A00%3A00&signature=vCSGGFyvxOyBXCh07CkmwhXgbNN9IDH5ygf40TI' \
        + 'DQ8o4me37e2mXNnt%2FjJVJop16rLJj3JK2U%2Flkwud6C1rqVw%3D%3D'
    callback_data =\
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
        cls.gate = Gate(cls.secret)

    def test_get_purchase_payment_page_url(self):
        payment = Payment('1')
        payment.payment_id = 'test-payment'
        payment.best_before = datetime(2055, 5, 5)
        payment.cashier_predefined_amounts = [1, 2, 3]
        purchase_payment_page_url = self.gate.get_purchase_payment_page_url(payment)
        url_parsed_params = urlparse.parse_qs(urlparse.urlparse(self.compare_url).query)
        gen_url_parsed_params = urlparse.parse_qs(urlparse.urlparse(purchase_payment_page_url).query)
        self.assertEqual(url_parsed_params, gen_url_parsed_params)

    def test_handle_callback(self):
        callback_data_raw = json.dumps(self.callback_data)
        callback = self.gate.handle_callback(callback_data_raw)
        self.assertTrue(isinstance(callback, Callback))
