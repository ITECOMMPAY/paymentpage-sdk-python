
from payment_page_sdk.signature_handler import SignatureHandler
from payment_page_sdk.process_exception import ProcessException
import json
import copy


class Callback(object):
    """Class for processing gate callback

    Attributes:
        SUCCESS_STATUS - Status of successful payment
        DECLINE_STATUS - Status of rejected payment
        AW_3DS_STATUS - Status of awaiting a request with the result of a 3-D Secure Verification
        AW_RED_STATUS - Status of awaiting customer return after redirecting the customer to an external provider system
        AW_CUS_STATUS - Status of awaiting customer actions, if the customer may perform additional attempts to make a
                        payment
        AW_CLA_STATUS - Status of awaiting additional parameters
        AW_CAP_STATUS - Status of awaiting request for withdrawal of funds (capture) or cancellation of payment (cancel)
                        from your project
        CANCELLED_STATUS - Status of holding of funds (produced on authorization request) is cancelled
        REFUNDED_STATUS - Status of successfully completed the full refund after a successful payment
        PART_REFUNDED_STATUS - Status of completed partial refund after a successful payment
        PROCESSING_STATUS - Status of payment processing at Gate
        ERROR_STATUS - Status of an error occurred while reviewing data for payment processing
        REVERSED_STATUS - Status of refund after a successful payment before closing of the business day
        __data - Callback data as dict
        __signatureHandler - SignatureHandler instance
    """
    SUCCESS_STATUS = 'success'
    DECLINE_STATUS = 'decline'
    AW_3DS_STATUS = 'awaiting 3ds result'
    AW_RED_STATUS = 'awaiting redirect result'
    AW_CUS_STATUS = 'awaiting customer'
    AW_CLA_STATUS = 'awaiting clarification'
    AW_CAP_STATUS = 'awaiting capture'
    CANCELLED_STATUS = 'cancelled'
    REFUNDED_STATUS = 'refunded'
    PART_REFUNDED_STATUS = 'partially refunded'
    PROCESSING_STATUS = 'processing'
    ERROR_STATUS = 'error'
    REVERSED_STATUS = 'reversed'

    __data = None
    __signatureHandler = None

    def __init__(self, data: str, signature_handler: SignatureHandler):
        """
        Callback constructor

        :param dict data:
        :param SignatureHandler signature_handler:
        """
        self.__data = self.decode_response(data)
        self.__signatureHandler = signature_handler
        if self.check_signature() == 0:
            raise ProcessException('Signature ' + self.get_signature() + ' is invalid')

    def get_payment(self):
        """
        Get payment info

        :return: mixed
        """
        return self.__get_value_by_name('payment')

    def get_payment_status(self) -> str:
        """
        Get payment status

        :return: str
        """
        return self.__get_value_by_name('status', self.get_payment())

    def get_payment_id(self) -> str:
        """
        Get payment ID

        :return: str
        """
        return self.__get_value_by_name('id', self.get_payment())

    def get_signature(self) -> str:
        """
        Get signature

        :return: str
        """
        return self.__get_value_by_name('signature')

    def decode_response(self, raw_data: str) -> dict:
        """
        Cast raw data to array

        :param str raw_data:
        :return: dict

        :raise: ProcessException
        """
        try:
            data = json.loads(raw_data)
        except ValueError:
            raise ProcessException('Error on response decoding')

        return data

    def check_signature(self) -> bool:
        """
        Check signature

        :return: bool
        """
        data = copy.deepcopy(self.__data)
        signature = self.get_signature()
        self.__remove_param('signature', data)

        return self.__signatureHandler.check(data['body'], signature)

    def __get_value_by_name(self, name: str, data: dict = {}):
        """
        Get value by name

        :param str name:
        :param dict data:
        :return:
        """
        if data == {}:
            data = self.__data

        if name in data:
            return data[name]

        for key in data:
            if isinstance(data[key], dict):
                sub_value = self.__get_value_by_name(name, data[key])
                if sub_value is not None:
                    return sub_value

        return None

    def __remove_param(self, name: str, data: dict):
        """
        Unset param at callback adata

        :param str name:
        :param dict data:
        :return: void
        """
        if name in data:
            del data[name]

        for key in data:
            if isinstance(data[key], dict):
                self.__remove_param(name, data[key])
