import urllib

from payment_page_sdk.signature_handler import SignatureHandler
from payment_page_sdk.payment_page import PaymentPage
from payment_page_sdk.callback import Callback
from payment_page_sdk.payment import Payment
from payment_page_sdk.validation_exception import ValidationException
from urllib.request import urlopen, Request
from urllib.error import HTTPError


class Gate(object):
    """Class Gate

    Attributes:
        CURRENCY_RUB - Currency RUB
        CURRENCY_USD - Currency USD
        CURRENCY_EUR - Currency EUR

        __paymentPageUrlBuilder - Builder for Payment page
        __signatureHandler - Signature Handler (check, sign)
        __validationUrl - Payment params validation domain with path to API
        __validatorEnabled - Enable (true) or disable (false) payment params validation
    """
    CURRENCY_RUB = 'RUB'
    CURRENCY_USD = 'USD'
    CURRENCY_EUR = 'EUR'

    __paymentPageUrlBuilder = None
    __signatureHandler = None
    __validationUrl = 'https://sdk.ecommpay.com/v1/params/check'
    __validatorEnabled = True

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
        if self.__validatorEnabled:
            self.validate(payment)

        return self.__paymentPageUrlBuilder.get_url(payment)

    def handle_callback(self, data):
        """
        Callback handler

        :param data:
        :return:
        """
        return Callback(data, self.__signatureHandler)

    def validate(self, payment: Payment):
        """
        Validate payment params before build payment link

        :param payment:
        :return:
        """
        paramsUrl = self.__validationUrl + '?' + urllib.parse.urlencode(payment.get_params())
        validationRequest = Request(paramsUrl)

        try:
            urlopen(validationRequest)
        except HTTPError as e:
            raise ValidationException(e)
