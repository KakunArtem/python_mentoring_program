from selenium.webdriver.common.by import By

from home_task_three.src.page_objects.base_page import BasePage


class LoginPage(BasePage):
    USER_NAME_INPUT_LOCATOR = (By.ID, "user-name")
    PASSWORD_INPUT_LOCATOR = (By.ID, "password")
    LOGIN_BUTTON_LOCATOR = (By.ID, "login-button")

    def enter_user_name(self, user_name):
        self.driver.find_element(*self.USER_NAME_INPUT_LOCATOR).send_keys(user_name)
        return self

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT_LOCATOR).send_keys(password)
        return self

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON_LOCATOR).click()
        return self
