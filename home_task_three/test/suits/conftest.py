import pytest
from home_task_three.src.clients import WebDriverClient, DriverTypes


@pytest.fixture(scope="module")
def driver():
    driver = WebDriverClient(DriverTypes.CHROME).get_client()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
