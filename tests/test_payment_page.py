
from payment_page_sdk.payment import Payment
from payment_page_sdk.payment_page import PaymentPage
from payment_page_sdk.signature_handler import SignatureHandler
from datetime import datetime
from urllib import parse as urlparse
import unittest


class PaymentPageTest(unittest.TestCase):
    compare_url = \
        'http://test.test/pay?best_before=2055-05-05T00%3A00%3A00&project_id=1&payment_id=test-payment&signature=' \
        + 'uiyaj9pCNt45hXe%2FyoyvXsdAqRvXLwg8a%2BUKrpvxG%2FGl18dh5NN1sdmbDoMG7%2BB8oZU9cycmOWoyo78etOjd0Q%3D%3D'
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
