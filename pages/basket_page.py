from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def assert_basket_has_no_products(self):
        self.is_not_element_present(
            *BasketPageLocators.PRODUCTS_IN_BASKET
        ), 'There should be no products in basket, but it contains some.'

    def assert_basket_empty_message(self):
        self.is_element_present(
            *BasketPageLocators.EMPTY_BASKET_MESSAGE
        ), 'Empty basket message not found, but there should be one.'
