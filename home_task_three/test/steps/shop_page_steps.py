from home_task_three.src.page_objects import ShopPage, SortingTypes, SideBar


class ShopPageSteps:
    def __init__(self, driver):
        self.shop_page = ShopPage(driver)
        self.sidebar = SideBar(driver)

    def add_items_to_cart(self, n_of_items):
        self.shop_page.add_items_to_chart(n_of_items)
        return self

    def remove_items_from_cart(self, n_of_items):
        self.shop_page.remove_items_from_chart(n_of_items)
        return self

    def open_cart(self):
        self.shop_page.open_cart()
        return self

    def sort_items(self, sorting_order=SortingTypes.PRICE_LOW_TO_HIGH):
        self.shop_page.sort_items(sorting_order)
        return self

    @staticmethod
    def sorting_by_name_test_data():
        return [
            {"sorting_type": SortingTypes.NAME_A_TO_Z, "assert": lambda my_list: my_list == sorted(my_list)},
            {"sorting_type": SortingTypes.NAME_Z_TO_A,
             "assert": lambda my_list: my_list == sorted(my_list, reverse=True)},
        ]

    @staticmethod
    def sorting_by_price_test_data():
        return [
            {"sorting_type": SortingTypes.PRICE_HIGH_TO_LOW,
             "assert": lambda my_list: ShopPageSteps.is_sorted_numerically(my_list, True)},
            {"sorting_type": SortingTypes.PRICE_LOW_TO_HIGH,
             "assert": lambda my_list: ShopPageSteps.is_sorted_numerically(my_list, False)},
        ]

    @staticmethod
    def is_sorted_numerically(price_list, reverse=False):
        float_prices = [float(price[1:]) for price in price_list]
        return float_prices == sorted(float_prices, reverse=reverse)

    def logout(self):
        self.sidebar.open_side_bar().click_logout()
        return self
