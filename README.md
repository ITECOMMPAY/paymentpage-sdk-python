# EcommPay payment page SDK

This is a set of libraries in the Python language to ease integration of your service
with the EcommPay Payment Page.

Please note that for correct SDK operating you must have at least Python 3.5.  

## Payment flow

![Payment flow](https://raw.githubusercontent.com/ITECOMMPAY/paymentpage-sdk-python/master/flow.png)

## Installation

Install with pip
```bash
pip install ecommpay-sdk
```

### Get URL for payment

```python
from payment_page_sdk.Gate import Gate
from payment_page_sdk.Payment import Payment

gate = Gate('secret')
payment = Payment(402)
payment.payment_amount = 1001
payment.payment_currency = 'USD'
payment_url = gate.get_purchase_payment_page_url(payment)
``` 

`payment_url` here is the signed URL.

### Handle callback from Ecommpay

You'll need to autoload this code in order to handle notifications:

```python
from payment_page_sdk.Gate import Gate

gate = Gate('secret')
callback = gate.handle_callback(data)
```

`data` is the JSON data received from payment system;

`callback` is the Callback object describing properties received from payment system;
`callback` implements these methods: 
1. `callback.get_payment_status();`
    Get payment status.
2. `callback.get_payment();`
    Get all payment data.
3. `callback.get_payment_id();`
    Get payment ID in your system.
