
import urllib.parse
from payment_page_sdk.signature_handler import SignatureHandler
from payment_page_sdk.payment import Payment


class PaymentPage(object):
    """Class PaymentPage for URL building

    Attributes:
        __baseUrl - Base URL for payment
        __signatureHandler - Signature Handler (check, sign)
    """
    __baseUrl = 'https://paymentpage.ecommpay.com/payment'
    __signatureHandler = None

    def __init__(self, signature_handler: SignatureHandler, base_url: str = ''):
        """
        PaymentPage constructor

        :param signature_handler:
        :param base_url:
        """
        self.__signatureHandler = signature_handler

        if base_url:
            self.__baseUrl = base_url

    def get_url(self, payment: Payment) -> str:
        """
        Get full URL for payment

        :param Payment payment:
        :return:
        """
        return self.__baseUrl + '?' \
            + urllib.parse.urlencode(payment.get_params()) \
            + '&signature=' + urllib.parse.quote_plus(self.__signatureHandler.sign(payment.get_params()))
