import pytest
from jsonschema import validate

from home_task_four.src.constants.data_store import DataStore
from home_task_four.src.http_reuqests import AuthRequest, PostsRequest
from home_task_four.src.schemas import PostsSchema


@pytest.fixture(scope="session", autouse=True)
def authorize_user():
    auth_endpoint = AuthRequest()

    DataStore.set_data("auth_token", auth_endpoint.auth_request())


class TestProductEndpoint:
    posts_endpoint = PostsRequest()

    """
    Validate that response schema is corresponds to the expected.
    In the scope of the mentoring program task, I will not create schema tests for all endpoints.
    """

    def test_validate_all_posts_schema(self):
        response = self.posts_endpoint.get_posts()
        validate(instance=response.body, schema=PostsSchema.get_all_posts_schema())

    """
    Validate that response include expected data.
    """

    def test_all_post_data(self):
        response = self.posts_endpoint.get_posts()

        assert response.status_code == 200
        # in case the total field can be updated, we should additionally check the number of rows available to users
        # (based on db information ex.)
        assert response.body['total'] == 150
        assert response.body['limit'] == 30

    """
    Validate that response include expected number of posts based on limits.
    """

    def test_limit_query_is_applied(self):
        limit = 3
        response = self.posts_endpoint.get_posts(limit)

        assert response.body['limit'] == limit
        assert len(response.body['posts']) == limit

    """
    Validate that it possible to get posts by user id
    """

    def test_get_post_by_user_id(self):
        response = self.posts_endpoint.get_posts(user_id="23")

        assert response.status_code == 200
        assert len(response.body['posts']) == 1

    """
    Validate that error returns if user id is invalid
    """

    def test_get_post_by_invalid_user_id(self):
        response = self.posts_endpoint.get_posts(user_id="invalid")

        assert response.status_code == 400
        assert response.body['message'] == "Invalid user id 'invalid'"
