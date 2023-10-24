from home_task_three.src.page_objects import CartPage


class CartPageSteps:
    def __init__(self, driver):
        self.cart_page = CartPage(driver)
