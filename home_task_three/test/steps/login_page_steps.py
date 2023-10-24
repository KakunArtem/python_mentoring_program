from home_task_three.src.clients import config
from home_task_three.src.page_objects import LoginPage


class LoginPageSteps:
    user_name = config.USER_NAME
    password = config.PASSWORD
    base_url = config.BASE_URL

    def __init__(self, driver):
        self.login_page = LoginPage(driver)

    def login(self, user_name=None, password=None):
        user_name = user_name or self.user_name
        password = password or self.password

        self.login_page.enter_user_name(user_name).enter_password(password).click_login_button()
        return self

    def open_login_page(self):
        self.login_page.driver.get(self.base_url)
        return self

    def login_button_is_visible(self):
        return self.login_page.driver.find_element(*self.login_page.LOGIN_BUTTON_LOCATOR).is_displayed()
