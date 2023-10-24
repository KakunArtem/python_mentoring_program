from jsonschema import validate

from home_task_four.src.http_reuqests.auth_request import AuthRequest
from home_task_four.src.schemas import AuthSchema


class TestAuthEndpoint:
    auth_endpoint = AuthRequest()

    """
    Validate that response schema is corresponds to the expected.
    """

    def test_validate_schema(self):
        response = self.auth_endpoint.auth_request()
        validate(instance=response.body, schema=AuthSchema.get_auth_schema())

    """
    Validate that the user gets valid information and a valid token when authenticating with valid creds.
    """

    def test_valid_creds(self):
        response = self.auth_endpoint.auth_request()

        assert response.body['email'] == 'kminchelle@qq.com'
        assert response.body['firstName'] == 'Jeanne'
        assert response.body['token']
        assert response.status_code == 200

    """
    Validate that the user gets proper error when authenticating with invalid creds.
    """

    def test_invalid_creds(self):
        invalid_creds = {
            'username': 'invalid',
            'password': 'invalid'
        }
        response = self.auth_endpoint.auth_request(invalid_creds)

        assert response.body['message'] == 'Invalid credentials'
        assert response.status_code == 400
