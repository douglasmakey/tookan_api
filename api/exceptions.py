# -*- coding: utf-8 -*-
from __future__ import unicode_literals

class APIError(Exception):
    def __init__(self, response, description):
        super(APIError, self).__init__(response.status_code, description)
        self.response = response
        self.description = description

    @property
    def status_code(self):
        return self.response.status_code

    @staticmethod
    def create_from_http_error(error):
        if error.response.status_code == 403:
            return Unauthorized(error.response)
        if error.response.status_code == 401:
            return InvalidCredentials(error.response)
        return APIError(error.response, error.response.reason)


class InvalidCredentials(APIError):
    def __init__(self, response):
        super(InvalidCredentials, self).__init__(response, "Invalid Credentials")


class Unauthorized(APIError):
    def __init__(self, response):
        super(Unauthorized, self).__init__(response, "Unauthorized")


class TransactionErrors(Exception):
    def __init__(self, response):
        error = self.extract_error(response)
        super(TransactionErrors, self).__init__(response.get('status'), error, response.get('message'))
        self.error = error
        self.status = response.get('status')
        self.message = response.get('message')

    @classmethod
    def extract_error(cls, response):
        if response.get('status') == 100:
            return 'PARAMETER_MISSING'
        elif response.get('status') == 101:
            return 'INVALID_KEY'
        elif response.get('status') == 200:
            return 'ACTION_COMPLETE'
        elif response.get('status') == 201:
            return 'SHOW_ERROR_MESSAGE'
        elif response.get('status') == 404:
            return 'ERROR_IN_EXECUTION'


