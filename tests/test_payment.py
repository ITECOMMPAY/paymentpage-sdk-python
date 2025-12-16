
from payment_page_sdk.payment import Payment
from datetime import datetime
import unittest

from tests.helpers.json_helper import load_json_from_file


class PaymentTest(unittest.TestCase):
    compare_data =\
        {
            'project_id': '1',
            'best_before': '2055-05-05T00:00:00',
            'interface_type': '{"id": 24}',
            'payment_id': 'test-payment',
            'operation_type': 'auth',
        }

    def test_get_params(self):
        payment = Payment('1')
        payment.payment_id = 'test-payment'
        payment.best_before = datetime(2055, 5, 5)
        payment.card_operation_type = 'auth'
        self.assertEqual(self.compare_data, payment.get_params())

    def test_set_booking_info(self):
        booking_info = load_json_from_file('/data/booking_info.json')
        payment = Payment('1')

        payment.set_booking_info(booking_info)

        self.assertEqual(
            "eyJzdGFydF9kYXRlIjogIjEyLTA4LTIwMjYiLCAiZW5kX2RhdGUiOiAiMTQtMDgtMjAyNiIsICJkZXNjcmlwdGlvbiI6ICJTaWRlcmlzIG11c2ljIGZlc3RpdmFsIGZ1bGwgcGFzcyIsICJ0b3RhbCI6IDIwMDAwMCwgInBheCI6IDIsICJib29rZXJzIjogW3siZmlyc3RfbmFtZSI6ICJXaWxsaWFtIiwgImxhc3RfbmFtZSI6ICJIZXJzY2hlbCIsICJlbWFpbCI6ICJyc2ZlbGxvd0BtYWlsLmNvbSJ9LCB7ImZpcnN0X25hbWUiOiAiQ2Fyb2xpbmUiLCAibGFzdF9uYW1lIjogIkhlcnNjaGVsIiwgImVtYWlsIjogInNhbGFyaWVkYXN0cm9ub21lckBtYWlsLmNvbSJ9XSwgIml0ZW1zIjogW3siZGVzY3JpcHRpb24iOiAiVklQIEFycml2YWwiLCAic3RhcnRfZGF0ZSI6ICIxMi0wOC0yMDI2IiwgImVuZF9kYXRlIjogIjEyLTA4LTIwMjYifSwgeyJkZXNjcmlwdGlvbiI6ICJIb3RlbCIsICJzdGFydF9kYXRlIjogIjEyLTA4LTIwMjYiLCAiZW5kX2RhdGUiOiAiMTQtMDgtMjAyNiJ9LCB7ImRlc2NyaXB0aW9uIjogIkNvbmNlcnRzIiwgInN0YXJ0X2RhdGUiOiAiMTItMDgtMjAyNiIsICJlbmRfZGF0ZSI6ICIxNC0wOC0yMDI2In0sIHsiZGVzY3JpcHRpb24iOiAiVklQIERlcGFydHVyZSIsICJzdGFydF9kYXRlIjogIjE0LTA4LTIwMjYiLCAiZW5kX2RhdGUiOiAiMTQtMDgtMjAyNiJ9XSwgInJlZmVyZW5jZSI6ICJtdXNpY2Zlc3RsaW5rIiwgImlkIjogIjgzIn0=",
            payment.get_params().get("booking_info")
        )
