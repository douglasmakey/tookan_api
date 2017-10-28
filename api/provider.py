import logging
import requests

from api.exceptions import Unauthorized, APIError, TransactionErrors

logger = logging.getLogger(__name__)

BASE_URL = 'https://api.tookanapp.com'
VERSION = 'v2'


class APIProvider(object):
    CONTENT_TYPE = 'application/json; charset=utf-8'

    def __init__(self, api_key, user_id):
        self.api_key = api_key
        self.user_id = user_id

    @classmethod
    def get_endpoint_url(cls, base_url, version, action):
        return "{}/{}/{}".format(base_url, version, action)

    @classmethod
    def do_request(cls, url, headers, payload):
        try:
            logger.debug("Requesting %s", url)

            response = requests.post(
                url,
                json=payload,
                headers=headers
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_error:
            raise APIError.create_from_http_error(http_error)

    @classmethod
    def validate_response(cls, response):
        if response.get('status') != 200:
            raise TransactionErrors(response)

    def request_resource(self, resource, action, payload):
        logger.debug('Resource: %s', resource)

        # Set api_key
        payload['api_key'] = self.api_key

        try:
            response = self.do_request(
                url=self.get_endpoint_url(base_url=BASE_URL, version=VERSION, action=action),
                headers=self._get_headers(),
                payload=payload
            )
        except Unauthorized:
            raise
        else:
            logger.debug('Response: %s', response)
            self.validate_response(response)
            return response

    def consume(self, resource, action, payload, with_user=False):
        if with_user:
            payload['user_id'] = self.user_id

        data = self.request_resource(resource=resource, action=action, payload=payload)
        return data

    def _get_headers(self):
        return {
            'Content-Type': self.CONTENT_TYPE,
        }
