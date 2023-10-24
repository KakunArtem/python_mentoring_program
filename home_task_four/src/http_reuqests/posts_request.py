import json

from home_task_four.src.clients import RequestClient, config
from home_task_four.src.constants.data_store import DataStore
from home_task_four.src.http_reuqests import Endpoints


class PostsRequest:
    def __init__(self):
        self.client = RequestClient()
        self.base_url = config.BASE_URL

    @staticmethod
    def _build_headers():
        auth_token = f'Bearer: {DataStore.get_data("auth_token")}'

        return {
            'Content-Type': 'application/json',
            'Authorization': auth_token
        }

    def get_posts(self, limit=None, user_id=None):
        url = f"{self.base_url}{Endpoints.POSTS}"
        if limit is not None:
            url += f"?limit={limit}"

        if user_id is not None:
            url += f"{Endpoints.POSTS_USERS}/{user_id}"

        response = self.client.make_request('GET', url=url, headers=self._build_headers())
        response.body = json.loads(response.text)

        return response

    def add_post(self, payload):
        url = f"{self.base_url}{Endpoints.POSTS_ADD}"

        response = self.client.make_request('POST', url=url, headers=self._build_headers(), payload=payload)
        response.body = json.loads(response.text)

        return response
