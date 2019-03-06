
from collections.abc import Iterable


class Payment(object):
    """Class Payment

    Attributes:
        str account_token: The token of the bank card that will be used to perform a payment
        str card_operation_type: Type of payment performed via payment card
        datetime best_before: Date and time when the payment period expires.
        bool close_on_missclick: A parameter that specifies the action of the widget (opened in the modal window) when a customer clicks outside the widget area.
        str css_modal_wrap: An additional CSS class for a modal window.
        str customer_id: Unique ID of the customer in your project
        bool force_acs_new_window: The forced display mode with the ACS page opening in a window despite the settings in Payment Page
        str force_payment_method: The ID of the payment provider that is opened to customers by default.
        str language_code: The language in which the payment page will be opened to the customer in ISO 639-1 alpha-2 format.
        str list_payment_block: The payment block on the list of payment methods.
        str merchant_fail_url: The URL of the page in your project to which a customer is returned after a failed payment.
        str merchant_success_url: The URL of the page in your project to which a customer is returned after a successful payment.
        str mode: Payment Page mode.
        int payment_amount: Payment amount specified in minor units of the currency of the payment
        str payment_currency: Payment currency in ISO 4217 alpha-3 format
        str payment_description: Payment description
        str payment_id: Unique ID of the payment in your project
        bool recurring_register: Parameter that indicates whether this payment should be registered as recurring
        str customer_first_name: Customer first name
        str customer_last_name: Customer last name
        str customer_phone: Customer phone number. Must have from 4 to 24 digits
        str customer_email: Customer e-mail
        str customer_country: Country of the customer address, in ISO 3166-1 alpha-2 format
        str customer_state: State or region of the customer address
        str customer_city: City of the customer address
        str customer_day_of_birth: Customer birth date, DD-MM-YYYY
        int customer_ssn: The last 4 digits of the social security number of US
        str billing_postal: The postal code of the customer billing address
        str billing_country: The country of the customer billing address, in ISO 3166-1 alpha-2 format
        str billing_region: The region or state of the customer billing address
        str billing_city: The city of the customer billing address
        str billing_address: The street of the customer billing address
        bool redirect: A parameter that enables opening of the generated payment page in a separate tab
        str redirect_fail_mode: The mode for customer redirection when the payment failed
        str redirect_fail_url: The URL of the page in your project to which the customer is redirected when the payment failed
        bool redirect_on_mobile: A parameter that enables opening of the generated payment page in a separate tab on mobile devices only
        str redirect_success_mode: The mode for customer redirection after a successful payment.
        str redirect_success_url: The URL of the page in your project to which the customer is redirected after a successful payment
        str redirect_tokenize_mode: The mode for customer redirection once a token is generated.
        str redirect_tokenize_url: The URL of the page in your project to which the customer is redirected after a successful token generation.
        str region_code: The region in ISO 3166-1 alpha-2 format. By default the region is determined by the IP address of the customer
        str target_element: The element in which the iframe of the payment page is embedded in the web page of your project.
        int terminal_id: Unique ID of the Payment Page template which you want to run despite the regional and A/B test settings
        str baseurl: Basic Payment Page address that is used in case the Payment Page domain differs from the domain used to connect libraries or if merchant.js is not connected via the <script> tag
        str payment_extra_param: Additional parameter to be forwarded to Gate

        PURCHASE_TYPE - Payment from customer account
        PAYOUT_TYPE - Payment to customer account
        RECURRING_TYPE - Recurring payment
    """
    PURCHASE_TYPE = 'purchase'
    PAYOUT_TYPE = 'payout'
    RECURRING_TYPE = 'recurring'

    def __init__(self, project_id: str, payment_id: str):
        """
        Payment constructor

        :param project_id: str
        """
        self.__dict__['project_id'] = project_id
        self.__dict__['payment_id'] = payment_id

    def get_params(self) -> dict:
        """
        Get payment parameters

        :return: dict
        """
        return self.__dict__

    def __setattr__(self, name, value):
        if name == 'best_before':
            value = value.isoformat()

        self.__dict__[name] = value
