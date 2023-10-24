import pytest

from home_task_four.src.constants.data_store import DataStore
from home_task_four.src.http_reuqests import AuthEndpoint


@pytest.fixture(scope="session", autouse=True)
def authorize_user():
    auth_endpoint = AuthEndpoint()
    DataStore.set_data("bearar")

class TestProductEndpoint:
