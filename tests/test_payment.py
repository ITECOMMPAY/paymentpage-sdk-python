
from payment_page_sdk.payment import Payment
from datetime import datetime
import unittest


class PaymentTest(unittest.TestCase):
    compare_data =\
        {
            'project_id': '1',
            'best_before': '2055-05-05T00:00:00',
            'interface_type': '{"id": 24}',
            'payment_id': 'test-payment'
        }

    def test_get_params(self):
        payment = Payment('1')
        payment.payment_id = 'test-payment'
        payment.best_before = datetime(2055, 5, 5)
        self.assertEqual(self.compare_data, payment.get_params())
