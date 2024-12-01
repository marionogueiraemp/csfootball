from django.core.exceptions import ValidationError
from rest_framework.exceptions import APIException


class PanelError(Exception):
    def __init__(self, message, code=None):
        self.message = message
        self.code = code
        super().__init__(self.message)


class PanelErrorHandler:
    @staticmethod
    def handle_refresh_error(error):
        if isinstance(error, APIException):
            return {'error': 'API Error', 'message': str(error)}
        return {'error': 'Refresh Failed', 'message': 'Unable to update panel data'}

    @staticmethod
    def handle_data_error(error):
        if isinstance(error, ValidationError):
            return {'error': 'Invalid Data', 'message': error.messages}
        return {'error': 'Data Error', 'message': 'Unable to process panel data'}
