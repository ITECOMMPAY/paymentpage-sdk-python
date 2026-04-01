
from payment_page_sdk.gate import Gate
from payment_page_sdk.payment import Payment
from datetime import datetime
from urllib import parse as urlparse
from payment_page_sdk.callback import Callback
import json
import unittest


class GateTest(unittest.TestCase):
    secret = 'qwerty'
    compare_url = \
        'https://paymentpage.ecommpay.com/payment?payment_id=test-payment&interface_type=%7B%22id%22%3A%2024%7D' \
        + '&project_id=60481&best_before=2055-05-05T00%3A00%3A00&signature=IC' \
        + 'BCw0eVO8mRjPs%2BRKBg97g1hvZojpTWPPd8v8SZTzT6Z7n7bbcW%2BH1eFXciRqSeo7xGP2Cy//3PdmuAvhBcvw=='
    callback_data =\
        {
            "payment":
                {
                    "id": "test-payment",
                    "status": "success"
                },
            "signature": "UGzKT0NC26f4u0niyJSQPx5q3kFFIndwLXeJVXahfCFwbY+Svg1WoXIxzrIyyjWUSLFhT8wAQ5SfBDRHnwm6Yg=="
        }

    @classmethod
    def setUp(cls):
        cls.gate = Gate(cls.secret)

    def test_get_purchase_payment_page_url(self):
        payment = Payment('60481', 'test-payment')
        payment.best_before = datetime(2055, 5, 5)
        purchase_payment_page_url = self.gate.get_purchase_payment_page_url(payment)
        url_parsed_params = urlparse.parse_qs(urlparse.urlparse(self.compare_url).query)
        gen_url_parsed_params = urlparse.parse_qs(urlparse.urlparse(purchase_payment_page_url).query)
        self.assertEqual(url_parsed_params, gen_url_parsed_params)

    def test_handle_callback(self):
        callback_data_raw = json.dumps(self.callback_data)
        callback = self.gate.handle_callback(callback_data_raw)
        self.assertTrue(isinstance(callback, Callback))
