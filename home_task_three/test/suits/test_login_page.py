from home_task_three.test.steps import LoginPageSteps, ShopPageSteps


class TestLoginPage:
    """
    Verify that a user can log in to the website with valid credentials
    """

    def test_login_with_valid_credentials(self, driver):
        login_steps = LoginPageSteps(driver)
        login_steps.open_login_page().login()

        shop_page_steps = ShopPageSteps(driver)

        assert shop_page_steps.shop_page.get_inventory_title() == 'Products'

    """
    Verify that a user can successfully logout
    """

    def test_logout(self, driver):
        login_steps = LoginPageSteps(driver)
        login_steps.open_login_page().login()

        shop_page_steps = ShopPageSteps(driver)
        shop_page_steps.logout()

        # For production tests, I would add an additional check that cookies/user data are deleted from local storage
        assert login_steps.login_button_is_visible()
