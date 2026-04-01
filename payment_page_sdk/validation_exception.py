
class ValidationException(Exception):
    """Validation request exception"""

    def __init__(self, *args):
        if args:
            self.validationResponseBody = args[0].read().decode()
            self.responseCode = self.args[0].status
        else:
            self.validationResponseBody = None

    def __str__(self):
        if self.validationResponseBody:
            return 'Response code - {0}, message - {1}'.format(self.responseCode, self.validationResponseBody)
        else:
            return 'Received a response without a message body'

