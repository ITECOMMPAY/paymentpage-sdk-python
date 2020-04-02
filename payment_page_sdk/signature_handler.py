
import base64
import hmac
from collections import OrderedDict


class SignatureHandler(object):
    """Class SignatureHandler

    Attributes:
        ITEMS_DELIMITER - signature concatenation delimiter
        IGNORE_KEYS - ignore keys in signature

        __secretKey - Secret key
    """
    ITEMS_DELIMITER = ';'
    IGNORE_KEYS = ['frame_mode']

    __secretKey = None

    def __init__(self, secret_key: str):
        """
        SignatureHandler constructor

        :param str secret_key:
        """
        self.__secretKey = secret_key

    def check(self, params: dict, signature):
        """
        Check signature

        :param dict params:
        :param signature:
        :return:
        """
        return self.sign(params) == signature

    def sign(self, params: dict) -> str:
        """
        Return signature

        :param params:
        :return:
        """
        secret_key = self.__secretKey.encode('utf-8')
        params_to_sign = self.__get_params_to_sign(params, self.IGNORE_KEYS)
        params_to_sign_list = list(OrderedDict(sorted(params_to_sign.items(), key=lambda t: t[0])).values())
        string_to_sign = self.ITEMS_DELIMITER.join(params_to_sign_list).encode('utf-8')

        return base64.b64encode(hmac.new(secret_key, string_to_sign, hmac._hashlib.sha512).digest()).decode()

    def __get_params_to_sign(self, params: dict, ignore=None, prefix='', sort=True) -> dict:
        """
        Get parameters to sign

        :param params:
        :param ignore:
        :param prefix:
        :param sort:
        :return:
        """
        if ignore is None:
            ignore = []

        params_to_sign = {}

        for key in params:
            if key in ignore:
                continue

            param_key = prefix + (':' if prefix else '') + key
            value = params[key]

            if isinstance(value, list):
                value = {str(key): value for key, value in enumerate(value)}

            if isinstance(value, dict):
                sub_array = self.__get_params_to_sign(value, ignore, param_key, False)
                params_to_sign.update(sub_array)
            else:
                if isinstance(value, bool):
                    value = '1' if value else '0'
                elif value is None:
                    value = ''
                else:
                    value = str(value)
                params_to_sign[param_key] = param_key + ':' + value

        if sort:
            sorted(params_to_sign.items(), key=lambda item: item[0])

        return params_to_sign
