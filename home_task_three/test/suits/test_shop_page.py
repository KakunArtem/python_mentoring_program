import pytest

from home_task_three.test.steps import LoginPageSteps, ShopPageSteps, CartPageSteps


class TestShopPage:
    """
    Verify that several items can be added to a chart
    """

    def test_item_added_to_chart(self, driver):
        number_of_items = 4

        login_steps = LoginPageSteps(driver)
        login_steps.open_login_page().login()

        shop_steps = ShopPageSteps(driver)
        shop_steps.add_items_to_cart(number_of_items).open_cart()

        cart_steps = CartPageSteps(driver)
        items_in_cart = cart_steps.cart_page.get_items_in_cart()

        assert len(items_in_cart) == number_of_items

    """
    Verify that items removed from a chart
    """

    def test_item_removed_from_chart(self, driver):
        number_of_items_to_add = 6
        number_of_items_to_remove = 3

        login_steps = LoginPageSteps(driver)
        login_steps.open_login_page().login()

        shop_steps = ShopPageSteps(driver)
        shop_steps \
            .add_items_to_cart(number_of_items_to_add) \
            .remove_items_from_cart(number_of_items_to_remove) \
            .open_cart()

        cart_steps = CartPageSteps(driver)
        items_in_cart = cart_steps.cart_page.get_items_in_cart()

        assert len(items_in_cart) == number_of_items_to_remove

    """
    Verify that sorting by name works as expected
    """

    @pytest.mark.parametrize('test_data', ShopPageSteps.sorting_by_name_test_data())
    def test_sorting_by_name(self, test_data, driver):
        login_steps = LoginPageSteps(driver)
        login_steps.open_login_page().login()

        shop_steps = ShopPageSteps(driver)
        shop_steps.sort_items(test_data.get("sorting_type"))
        item_names = shop_steps.shop_page.get_inventory_titles()

        assert test_data.get("assert")(item_names)

    """
    Verify that sorting by price works as expected
    """

    @pytest.mark.parametrize('test_data', ShopPageSteps.sorting_by_price_test_data())
    def test_sorting_by_price(self, test_data, driver):
        login_steps = LoginPageSteps(driver)
        login_steps.open_login_page().login()

        shop_steps = ShopPageSteps(driver)
        shop_steps.sort_items(test_data.get("sorting_type"))
        item_names = shop_steps.shop_page.get_inventory_prices()

        assert test_data.get("assert")(item_names)
