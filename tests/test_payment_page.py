
from payment_page_sdk.payment import Payment
from payment_page_sdk.payment_page import PaymentPage
from payment_page_sdk.signature_handler import SignatureHandler
from datetime import datetime
from urllib import parse as urlparse
import unittest


class PaymentPageTest(unittest.TestCase):
    compare_url = \
        'http://test.test/pay?best_before=2055-05-05T00%3A00%3A00&interface_type=%7B%22id%22%3A%2024%7D&project_id=1&payment_id=test-payment&signature=' \
        + 'q69mSGul5x6KACTn0Vl%2BX6N4hH1lL45yQiEbmLzJvNoJ1hwkBuiEv%2FLLpJuyLWtIrgU7%2Bq0TAUO0f%2Bai0bqjKQ%3D%3D'
    secret = 'qwerty'

    @classmethod
    def setUp(cls):
        signature_handler = SignatureHandler(cls.secret)
        cls.payment_page = PaymentPage(signature_handler, 'http://test.test/pay')

    def test_get_url(self):
        payment = Payment('1', 'test-payment')
        payment.best_before = datetime(2055, 5, 5)
        self.assertEqual(
            urlparse.parse_qs(urlparse.urlparse(self.compare_url).query),
            urlparse.parse_qs(urlparse.urlparse(self.payment_page.get_url(payment)).query)
        )
