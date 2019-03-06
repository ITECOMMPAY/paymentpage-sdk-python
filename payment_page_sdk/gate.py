
from payment_page_sdk.signature_handler import SignatureHandler
from payment_page_sdk.payment_page import PaymentPage
from payment_page_sdk.callback import Callback
from payment_page_sdk.payment import Payment


class Gate(object):
    """Class Gate

    Attributes:
        CURRENCY_RUB - Currency RUB
        CURRENCY_USD - Currency USD
        CURRENCY_EUR - Currency EUR

        __paymentPageUrlBuilder - Builder for Payment page
        __signatureHandler - Signature Handler (check, sign)
    """
    CURRENCY_RUB = 'RUB'
    CURRENCY_USD = 'USD'
    CURRENCY_EUR = 'EUR'

    __paymentPageUrlBuilder = None
    __signatureHandler = None

    def __init__(self, secret: str, base_url: str = ''):
        """
        Gate constructor

        :param str secret: Secret key
        """
        self.__signatureHandler = SignatureHandler(secret)
        self.__paymentPageUrlBuilder = PaymentPage(self.__signatureHandler, base_url)

    def get_purchase_payment_page_url(self, payment: Payment) -> str:
        """
        Get URL for purchase payment page

        :param Payment payment:
        :return:
        """
        return self.__paymentPageUrlBuilder.get_url(payment)

    def handle_callback(self, data):
        """
        Callback handler

        :param data:
        :return:
        """
        return Callback(data, self.__signatureHandler)
