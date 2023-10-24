import json

from home_task_four.src.clients import RequestClient, config
from home_task_four.src.http_reuqests.endpoints_enum import Endpoints


class AuthEndpoint:
    def __init__(self):
        self.client = RequestClient()
        self.base_url = config.BASE_URL

    @staticmethod
    def _build_headers():
        return {
            'Content-Type': 'application/json'
        }

    def _build_url(self):
        return self.base_url + Endpoints.AUTH

    def auth_request(self, creds=None):
        if creds is None:
            creds = {"username": config.USER_NAME, "password": config.PASSWORD}

        response = self.client.make_request('POST',
                                            url=self._build_url(),
                                            headers=self._build_headers(),
                                            payload=creds)

        response.body = json.loads(response.text)

        return response
