import allure

from pages import BasePage


class BasketPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.url = self.browser.current_url

        self.products_in_basket_locator = ('id', 'basket_formset')
        self.empty_basket_message_locator = (
            'css selector',
            '#content_inner > p',
        )

    @allure.step('Assert basket has no products')
    def assert_basket_has_no_products(self):
        self.is_not_element_present(
            *self.products_in_basket_locator
        ), 'There should be no products in basket, but it contains some'

    @allure.step('Assert basket has message that it is empty')
    def assert_basket_empty_message(self):
        self.is_element_present(
            *self.empty_basket_message_locator
        ), 'Empty basket message is not displayed, but should be'
