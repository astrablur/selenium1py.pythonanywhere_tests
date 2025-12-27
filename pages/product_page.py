from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def assert_basket_messages(self):
        self.assert_success_message()
        self.assert_product_name_matches_original_product_name()
        self.assert_product_price_matches_original_product_price()

    def assert_product_name_matches_original_product_name(self):
        original_product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
        ).text
        product_name_in_alert = self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE
        ).text

        assert original_product_name == product_name_in_alert, (
            f'Product name should be "{original_product_name}", '
            f'but product name in alert is "{product_name_in_alert}"'
        )

    def assert_product_price_matches_original_product_price(self):
        original_product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text
        msg_with_product_price_in_alert = self.browser.find_element(
            *ProductPageLocators.BASKET_PRICE_MESSAGE
        ).text

        assert original_product_price == msg_with_product_price_in_alert, (
            f'Basket price should be "{original_product_price}", '
            f'but basket price in alert is "{msg_with_product_price_in_alert}"'
        )

    def assert_success_message(self):
        self.is_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), 'Success message is not displayed'

    def assert_success_message_disappeared(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), 'Success message is presented, but should disappear'

    def click_add_to_basket_button(self):
        self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        ).click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), 'Success message is presented, but should not be'
