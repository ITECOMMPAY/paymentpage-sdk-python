
from payment_page_sdk.signature_handler import SignatureHandler
from payment_page_sdk.callback import Callback
import unittest


class CallbackFormatsTest(unittest.TestCase):
    secret = 'qwerty'
    cases =\
        [
            "{\n" +
            "    \"general\":{\n" +
            "        \"signature\":\"O5nJHj7yS4/6XC81VijFZFtEVhr6+OJ8Rb4FaRmHWR9Ti2H9L9jcvS8f9x2hQ5NgQQwlsEocrTb+YrDfnsSVHQ==\"\n" +
            "    },\n" +
            "    \"project_id\":\"[2] projectId\",\n" +
            "    \"payment\":{\n" +
            "        \"id\":\"[40] paymentId\",\n" +
            "        \"type\":\"[26] transactionType\",\n" +
            "        \"status\":\"[27] transactionStatus\",\n" +
            "        \"description\":\"[44] description\",\n" +
            "        \"date\":\"[30] internalProcessingDateTime\",\n" +
            "        \"method\":\"[17] paymentMethodTitle\",\n" +
            "        \"sum\":\"[23] transactionSum\",\n" +
            "        \"merchant_refund_id\":\"[451] merchantRefundId\"\n" +
            "    },\n" +
            "    \"account\":{\n" +
            "        \"token\":\"[41] token\",\n" +
            "        \"number\":\"[56] accountNumber\"\n" +
            "    },\n" +
            "    \"customer\":{\n" +
            "        \"id\":\"[18] userLogin\",\n" +
            "        \"phone\":\"[76] phone\"\n" +
            "    },\n" +
            "    \"clarification_fields\":\"[82] clarificationFields\",\n" +
            "    \"avs_result\":\"[83] avsResult\",\n" +
            "    \"provider_extra_fields\":\"[90] providerExtraFields\",\n" +
            "    \"recurring\":{\n" +
            "        \"id\":\"[100] id\",\n" +
            "        \"currency\":\"[107] currency\",\n" +
            "        \"valid_thru\":\"[108] valid_thru\"\n" +
            "    },\n" +
            "    \"operation\":{\n" +
            "        \"id\":\"[192] operation_id\",\n" +
            "        \"type\":\"[193] operation_type\",\n" +
            "        \"status\":\"[194] operation_status\",\n" +
            "        \"date\":\"[195] operation_date\",\n" +
            "        \"created_date\":\"[196] operation_created_date\",\n" +
            "        \"request_id\":\"[197] operation_request_id\",\n" +
            "        \"sum_initial\":{\n" +
            "            \"amount\":\"[198] operation_sum_initial_amount\",\n" +
            "            \"currency\":\"[199] operation_sum_initial_currency\"\n" +
            "        },\n" +
            "        \"sum_converted\":{\n" +
            "            \"amount\":\"[200] operation_sum_converted_amount\",\n" +
            "            \"currency\":\"[201] operation_sum_converted_currency\"\n" +
            "        },\n" +
            "        \"code\":\"[202] operation_code\",\n" +
            "        \"message\":\"[203] operation_message\",\n" +
            "        \"eci\":\"[205] operation_eci\",\n" +
            "        \"provider\":{\n" +
            "            \"id\":\"[206] operation_provider_id\",\n" +
            "            \"payment_id\":\"[207] operation_provider_payment_id\",\n" +
            "            \"auth_code\":\"[210] operation_provider_auth_code\",\n" +
            "            \"endpoint_id\":\"[211] operation_provider_endpoint_id\",\n" +
            "            \"date\":\"[212] operation_provider_date\"\n" +
            "        }\n" +
            "    }\n" +
            "}",
            "{\n" +
            "    \"general\":{\n" +
            "        \"signature\":\"R5wq+3/y4lG9ty5sHR6MuscWBRg/bzAo9dxlMkVOUhQ+KpS7FwHMx+5saiLQnn90Rl7rhp1U37dgThSorpn1Ew==\",\n" +
            "        \"project_id\":\"[2] projectId\"\n" +
            "    },\n" +
            "    \"request\":{\n" +
            "        \"action\":\"[36] action\",\n" +
            "        \"errors\":\"[38] errors\",\n" +
            "        \"id\":\"[3] requestId\",\n" +
            "        \"status\":\"[37] status\"\n" +
            "    },\n" +
            "    \"customer\":{\n" +
            "        \"id\":\"[18] userLogin\"\n" +
            "    },\n" +
            "    \"token_status\":\"[71] status\",\n" +
            "    \"token_created_at\":\"[70] created_at\",\n" +
            "    \"token\":\"[68] tokenString\"\n" +
            "}",
            "{\n" +
            "    \"general\":{\n" +
            "        \"signature\":\"+XNqUNPEo/mr1I3H/tGRCnNoWxqyqpzQIRIWv3eXfEzhfrqdZXHKHOWYlVryp1WayLTImLSqNUaDoqi3/G/y9w==\"\n" +
            "    },\n" +
            "    \"project_id\":\"[2] projectId\",\n" +
            "    \"recurring\":{\n" +
            "        \"id\":\"[100] id\",\n" +
            "        \"status\":\"[101] status\",\n" +
            "        \"type\":\"[102] type\",\n" +
            "        \"currency\":\"[107] currency\",\n" +
            "        \"exp_year\":\"[103] exp_year\",\n" +
            "        \"exp_month\":\"[104] exp_month\",\n" +
            "        \"period\":\"[105] period\",\n" +
            "        \"time\":\"[106] time\"\n" +
            "    }\n" +
            "}",
            "{\n" +
            "    \"general\":{\n" +
            "        \"signature\":\"Cm0L/+dLPg6Au/jEG0yr1FktzA1QwojRp95R9o5O4Wxx6MzjwTrso5B4rBXekM/fp5znut0WVGLFGG+TtJjuHQ==\"\n" +
            "    },\n" +
            "    \"redirectData\":{\n" +
            "        \"method\":\"GET\",\n" +
            "        \"body\":[\n" +
            "            \n" +
            "        ],\n" +
            "        \"encrypted\":[\n" +
            "            \n" +
            "        ],\n" +
            "        \"url\":\"url data\"\n" +
            "    },\n" +
            "    \"payment\":{\n" +
            "        \"id\":\"qwerty123\"\n" +
            "    }\n" +
            "}",
            "{\n" +
            "    \"general\":{\n" +
            "        \"signature\":\"NpJuOiG6jSzh6CDNBYT9fqKZs9PkaXZQr3aqaN5yTvZdFj1sJaqWEhl1o4wCxyen2w0VhwdJ8p6ddplEqMWhUg==\",\n" +
            "        \"project_id\":\"[2] projectId\"\n" +
            "    },\n" +
            "    \"card\":{\n" +
            "        \"exp_month\":\"[73] month\",\n" +
            "        \"exp_year\":\"[72] year\",\n" +
            "        \"holder\":\"[74] holderName\",\n" +
            "        \"number\":\"[21] cardPanMasked\"\n" +
            "    },\n" +
            "    \"request\":{\n" +
            "        \"action\":\"[36] action\",\n" +
            "        \"errors\":\"[38] errors\",\n" +
            "        \"status\":\"[37] status\",\n" +
            "        \"id\":\"[3] requestId\"\n" +
            "    },\n" +
            "    \"customer\":{\n" +
            "        \"id\":\"[18] userLogin\"\n" +
            "    },\n" +
            "    \"token_status\":\"[71] status\",\n" +
            "    \"token_created_at\":\"[70] created_at\",\n" +
            "    \"token\":\"[68] tokenString\"\n" +
            "}",
            "{\n" +
            "    \"general\":{\n" +
            "        \"signature\":\"FZWW+aSwLzMDpS7A1IVNZ6uLYHphXIX8e9zdkHQB9IAqqWXKB5f/21vci2dv3h+kIB2kqTY2OKZCURs6v0th/w==\"\n" +
            "    },\n" +
            "    \"operation\":{\n" +
            "        \"sum_initial\":{\n" +
            "            \"amount\":\"[198] operation_sum_initial_amount\",\n" +
            "            \"currency\":\"[199] operation_sum_initial_currency\"\n" +
            "        },\n" +
            "        \"sum_converted\":{\n" +
            "            \"amount\":\"[200] operation_sum_converted_amount\",\n" +
            "            \"currency\":\"[201] operation_sum_converted_currency\"\n" +
            "        },\n" +
            "        \"eci\":\"[205] operation_eci\",\n" +
            "        \"provider\":{\n" +
            "            \"id\":\"[206] operation_provider_id\",\n" +
            "            \"payment_id\":\"[207] operation_provider_payment_id\",\n" +
            "            \"auth_code\":\"[210] operation_provider_auth_code\",\n" +
            "            \"endpoint_id\":\"[211] operation_provider_endpoint_id\",\n" +
            "            \"date\":\"[212] operation_provider_date\"\n" +
            "        },\n" +
            "        \"id\":\"[192] operation_id\",\n" +
            "        \"type\":\"[193] operation_type\",\n" +
            "        \"status\":\"[194] operation_status\",\n" +
            "        \"date\":\"[195] operation_date\",\n" +
            "        \"created_date\":\"[196] operation_created_date\",\n" +
            "        \"request_id\":\"[197] operation_request_id\"\n" +
            "    },\n" +
            "    \"customer\":{\n" +
            "        \"phone\":\"[76] phone\",\n" +
            "        \"id\":\"[18] userLogin\"\n" +
            "    },\n" +
            "    \"recurring\":{\n" +
            "        \"id\":\"[100] id\",\n" +
            "        \"currency\":\"[107] currency\",\n" +
            "        \"valid_thru\":\"[108] valid_thru\"\n" +
            "    },\n" +
            "    \"provider_extra_fields\":\"[90] providerExtraFields\",\n" +
            "    \"clarification_fields\":\"[82] clarificationFields\",\n" +
            "    \"avs_result\":\"[83] avsResult\",\n" +
            "    \"account\":{\n" +
            "        \"token\":\"[41] token\",\n" +
            "        \"number\":\"[56] accountNumber\"\n" +
            "    },\n" +
            "    \"project_id\":\"[2] projectId\",\n" +
            "    \"payment\":{\n" +
            "        \"id\":\"[40] paymentId\",\n" +
            "        \"type\":\"[26] transactionType\",\n" +
            "        \"status\":\"[27] transactionStatus\",\n" +
            "        \"description\":\"[44] description\",\n" +
            "        \"date\":\"[30] internalProcessingDateTime\",\n" +
            "        \"method\":\"[17] paymentMethodTitle\",\n" +
            "        \"sum\":\"[23] transactionSum\"\n" +
            "    },\n" +
            "    \"errors\":\"[38] errors\"\n" +
            "}",
            "{\n" +
            "    \"general\":{\n" +
            "        \"project_id\":\"[43] site_id\",\n" +
            "        \"payment_id\":\"[39] order_id\",\n" +
            "        \"signature\":\"q1aOeD+qH3L050pmRbw65p6vmUqMKT6f0hu1xGgMuh77Z9wDQvV7ySDH1y/mjFqy9Sc1qbnLDp2U83U8bWarIg==\"\n" +
            "    },\n" +
            "    \"threeds2\":\"[171] threeds2\",\n" +
            "    \"display_data\":\"[141] displayData\",\n" +
            "    \"additional_terminal_data\":\"[127] terminalAdditionalInfo\",\n" +
            "    \"payment\":{\n" +
            "        \"cascading_with_redirect\":\"[125] cascadingRedirect\",\n" +
            "        \"is_new_attempts_available\":\"[66] isNewAttemptsAvailable\",\n" +
            "        \"attempts_timeout\":\"[67] attemptsTimeout\",\n" +
            "        \"provider_id\":\"[45] id\",\n" +
            "        \"status\":\"[57] transactionStatusNonMapped\",\n" +
            "        \"id\":\"[40] paymentId\",\n" +
            "        \"method\":\"[17] paymentMethodTitle\",\n" +
            "        \"date\":\"[30] internalProcessingDateTime\",\n" +
            "        \"result_code\":\"[33] processorCode\",\n" +
            "        \"result_message\":\"[34] processorMessage\",\n" +
            "        \"split_with_redirect\":\"[381] splitWithRedirect\"\n" +
            "    },\n" +
            "    \"provider_extra_fields\":\"[90] providerExtraFields\",\n" +
            "    \"rrn\":\"[110] rrn\",\n" +
            "    \"AuthCode\":\"[31] authCode\",\n" +
            "    \"return_url\":\"[113] redirectData\",\n" +
            "    \"qr_code\":\"[114] qrCodeData\",\n" +
            "    \"acs\":\"[12] acsData\",\n" +
            "    \"clarification_fields\":\"[82] clarificationFields\",\n" +
            "    \"avs_result\":\"[83] avsResult\",\n" +
            "    \"account\":{\n" +
            "        \"number\":\"[56] accountNumber\",\n" +
            "        \"token\":\"[41] token\"\n" +
            "    },\n" +
            "    \"customer\":{\n" +
            "        \"id\":\"[18] userLogin\"\n" +
            "    },\n" +
            "    \"errors\":\"[38] errors\",\n" +
            "    \"request_id\":\"[3] requestId\",\n" +
            "    \"transaction\":{\n" +
            "        \"id\":\"[1] transactionId\",\n" +
            "        \"date\":\"[30] internalProcessingDateTime\",\n" +
            "        \"type\":\"[26] transactionType\"\n" +
            "    },\n" +
            "    \"description\":\"[44] description\",\n" +
            "    \"sum_request\":{\n" +
            "        \"amount\":\"[48] amount_incoming\",\n" +
            "        \"currency\":\"[49] currency_incoming\"\n" +
            "    },\n" +
            "    \"sum_real\":{\n" +
            "        \"amount\":\"[24] transactionAmountChannel\",\n" +
            "        \"currency\":\"[25] transactionCurrencyChannel\"\n" +
            "    },\n" +
            "    \"sum_refund\":{\n" +
            "        \"amount\":\"[46] transactionAmountRefund\",\n" +
            "        \"currency\":\"[47] transactionCurrencyRefund\"\n" +
            "    }\n" +
            "}",
            "{\n" +
            "    \"general\":{\n" +
            "        \"project_id\":\"[2] projectId\",\n" +
            "        \"signature\":\"OIRodGzsjGGrrKpvH0hOE64zNKBrS7SvGbzxYSyhLmsoPCv2KuFXXQ6LXML7UnZWyLsvHfNV5TS0x4zmP0vXCw==\"\n" +
            "    },\n" +
            "    \"card\":{\n" +
            "        \"exp_month\":\"[73] month\",\n" +
            "        \"exp_year\":\"[72] year\",\n" +
            "        \"holder\":\"[74] holderName\",\n" +
            "        \"number\":\"[21] cardPanMasked\",\n" +
            "        \"country\":\"[86] country\",\n" +
            "        \"issuer_name\":\"[88] issuer_name\"\n" +
            "    },\n" +
            "    \"request\":{\n" +
            "        \"action\":\"[36] action\",\n" +
            "        \"errors\":\"[38] errors\",\n" +
            "        \"status\":\"[37] status\",\n" +
            "        \"id\":\"[3] requestId\"\n" +
            "    },\n" +
            "    \"customer\":{\n" +
            "        \"id\":\"[18] userLogin\"\n" +
            "    },\n" +
            "    \"token_status\":\"[71] status\",\n" +
            "    \"token_created_at\":\"[70] created_at\",\n" +
            "    \"token\":\"[68] tokenString\"\n" +
            "}",
        ]

    @classmethod
    def setUp(cls):
        cls.signature_handler = SignatureHandler("123")

    def test_formats(self):
        for callback_data in self.cases:
            callback = Callback(callback_data, self.signature_handler)
            callback.get_payment()
            callback.get_payment_id()
            callback.get_payment_status()
