import json
import logging

import requests

from home_task_four.src.clients.configuration import config


class RequestException(Exception):
    def __init__(self, method, url, payload, headers):
        self.message = f"""An error occurred while processing a request:
        method: {method}
        url: {url}
        headers: {headers}
        payload: {payload}
        """
        super().__init__(self.message)


class RequestClient:
    @staticmethod
    def make_request(method, url, payload, headers):
        try:
            response = requests.request(method, url, headers=headers, data=json.dumps(payload))
        except Exception as e:
            raise RequestException(method, url, payload, headers)

        return response

    @staticmethod
    def get_request_client() -> requests:
        return requests
