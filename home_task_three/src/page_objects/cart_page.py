from selenium.webdriver.common.by import By

from home_task_three.src.page_objects.base_page import BasePage


class CartPage(BasePage):
    CART_ELEMENTS_LOCATOR = (By.CLASS_NAME, "cart_item")

    def get_items_in_cart(self):
        return self.driver.find_elements(*self.CART_ELEMENTS_LOCATOR)
