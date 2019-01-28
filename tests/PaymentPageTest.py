
from payment_page_sdk.Payment import Payment
from payment_page_sdk.PaymentPage import PaymentPage
from payment_page_sdk.SignatureHandler import SignatureHandler
from datetime import datetime
from urllib import parse as urlparse
import unittest


class PaymentPageTest(unittest.TestCase):
    compare_url = \
        'https://paymentpage.ecommpay.com/payment?best_before=2055-05-05T00%3A00%3A00&cashier_predefined_amounts=' \
        + '1%2C2%2C3&project_id=1&payment_id=test-payment&signature=vCSGGFyvxOyBXCh07CkmwhXgbNN9IDH5ygf40TIDQ8o4m' \
        + 'e37e2mXNnt%2FjJVJop16rLJj3JK2U%2Flkwud6C1rqVw%3D%3D'
    secret = 'qwerty'

    @classmethod
    def setUp(cls):
        signature_handler = SignatureHandler(cls.secret)
        cls.payment_page = PaymentPage(signature_handler)

    def test_get_url(self):
        payment = Payment('1')
        payment.payment_id = 'test-payment'
        payment.best_before = datetime(2055, 5, 5)
        payment.cashier_predefined_amounts = [1, 2, 3]
        self.assertEqual(
            urlparse.parse_qs(urlparse.urlparse(self.compare_url).query),
            urlparse.parse_qs(urlparse.urlparse(self.payment_page.get_url(payment)).query)
        )
