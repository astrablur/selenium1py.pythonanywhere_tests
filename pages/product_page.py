from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_basket_button(self):
        self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        ).click()

    def assert_successful_msg(self):
        self.is_element_present(
            *ProductPageLocators.SUCCESS_MSG
        ), 'Success message is not displayed'

    def assert_product_name_matches_original_product_name(self):
        original_product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
        ).text
        product_name_in_alert = self.browser.find_element(
            *ProductPageLocators.SUCCESS_MSG
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
            *ProductPageLocators.BASKET_PRICE_MSG
        ).text

        assert original_product_price == msg_with_product_price_in_alert, (
            f'Basket price should be "{original_product_price}", '
            f'but basket price in alert is "{msg_with_product_price_in_alert}"'
        )

    def assert_basket_messages(self):
        self.assert_successful_msg()
        self.assert_product_name_matches_original_product_name()
        self.assert_product_price_matches_original_product_price()
