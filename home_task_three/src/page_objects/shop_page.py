from selenium.webdriver.common.by import By

from home_task_three.src.page_objects.base_page import BasePage


class SortingTypes:
    NAME_A_TO_Z = 'az'
    NAME_Z_TO_A = 'za'
    PRICE_HIGH_TO_LOW = 'hilo'
    PRICE_LOW_TO_HIGH = 'lohi'


class SideBar(BasePage):
    BURGER_MENU_LOCATOR = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    LOGOUT_LOCATOR = (By.XPATH, "//a[@id='logout_sidebar_link']")

    def open_side_bar(self):
        self.driver.find_element(*self.BURGER_MENU_LOCATOR).click()
        return self

    def click_logout(self):
        self.driver.find_element(*self.LOGOUT_LOCATOR).click()
        return self

class ShopPage(BasePage):
    ADD_TO_CART_LOCATOR = (By.XPATH, "//*[contains(text(),'Add to cart')]")
    REMOVE_FROM_CART_LOCATOR = (By.XPATH, "//*[contains(text(),'Remove')]")
    CART_LOCATOR = (By.CLASS_NAME, "shopping_cart_container")
    SORT_CONTAINER_LOCATOR = (By.CLASS_NAME, "product_sort_container")
    INVENTORY_ITEMS_NAME_LOCATOR = (By.XPATH, "//div[@class='inventory_item_name']")
    INVENTORY_ITEMS_PRICE_LOCATOR = (By.XPATH, "//div[@class='inventory_item_price']")
    INVENTORY_TITLE_LOCATOR = (By.XPATH, "//span[@class='title']")

    def SORTING_TYPE_LOCATOR(self, sorting_type):
        return (By.XPATH, f"//option[@value='{sorting_type}']")

    def get_inventory_title(self):
        return self.driver.find_element(*self.INVENTORY_TITLE_LOCATOR).text

    def add_items_to_chart(self, n_of_items):
        items = self.driver.find_elements(*self.ADD_TO_CART_LOCATOR)

        for item in items[:n_of_items]:
            item.click()
        return self

    def remove_items_from_chart(self, n_of_items):
        items = self.driver.find_elements(*self.REMOVE_FROM_CART_LOCATOR)

        for item in items[:n_of_items]:
            item.click()
        return self

    def open_cart(self):
        self.driver.find_element(*self.CART_LOCATOR).click()
        return self

    def sort_items(self, sorting_order: SortingTypes):
        self.driver.find_element(*self.SORT_CONTAINER_LOCATOR).click()
        self.driver.find_element(*self.SORTING_TYPE_LOCATOR(sorting_order)).click()
        return self

    def get_inventory_titles(self):
        inventory_items = self.driver.find_elements(*self.INVENTORY_ITEMS_NAME_LOCATOR)
        return [item.text for item in inventory_items]

    def get_inventory_prices(self):
        inventory_items = self.driver.find_elements(*self.INVENTORY_ITEMS_PRICE_LOCATOR)
        return [item.text for item in inventory_items]
