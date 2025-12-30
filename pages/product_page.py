import allure

from pages import BasePage


class ProductPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.url = None

        self.product_name_locator = ('css selector', '.product_main h1')
        self.product_price_locator = (
            'css selector',
            '.product_main .price_color',
        )

        self.add_to_basket_button_locator = (
            'css selector',
            '.btn-add-to-basket',
        )
        self.success_message_locator = (
            'css selector',
            '.alert-success:nth-child(1) .alertinner strong',
        )
        self.basket_price_locator = ('css selector', '.alert-info strong')

    @property
    def add_to_basket_button(self):
        return self.find_element(*self.add_to_basket_button_locator)

    @property
    def basket_price(self):
        return self.find_element(*self.basket_price_locator)

    @property
    def product_name(self):
        return self.find_element(*self.product_name_locator)

    @property
    def product_price(self):
        return self.find_element(*self.product_price_locator)

    @property
    def success_message(self):
        return self.find_element(*self.success_message_locator)

    @allure.step('Assert Add to basket button is present and active')
    def assert_add_to_basket_button_is_present_and_active(self):
        self.is_element_present(
            *self.add_to_basket_button_locator
        ), 'Add to basket button is not present, but should be'

        assert (
            self.add_to_basket_button.is_displayed()
        ), 'Add to basket button is not displayed, but should be.'
        assert (
            self.add_to_basket_button.is_enabled()
        ), 'Add to basket button is not enabled, but should be.'

    @allure.step(
        'Assert alert basket message with product added to basket is displayed'
    )
    def assert_basket_messages(self):
        self.assert_success_message()
        self.assert_product_name_matches_original_product_name()
        self.assert_product_price_matches_original_product_price()

    def assert_product_name_matches_original_product_name(self):
        original_product_name = self.product_name.text
        product_name_in_alert = self.success_message.text

        assert original_product_name == product_name_in_alert, (
            f'Product name should be "{original_product_name}", '
            f'but product name in alert is "{product_name_in_alert}"'
        )

    def assert_product_price_matches_original_product_price(self):
        original_product_price = self.product_price.text
        basket_product_price = self.basket_price.text

        assert original_product_price == basket_product_price, (
            f'Basket price should be "{original_product_price}", '
            f'but basket price in alert is "{basket_product_price}"'
        )

    def assert_success_message(self):
        self.is_element_present(
            *self.success_message_locator
        ), 'Success message is not displayed, but should be'

    @allure.step('Click add to basket button')
    def click_add_to_basket_button(self):
        self.add_to_basket_button.click()

    @allure.step('Open Product page')
    def open_product_page(self, link):
        self.open(link)

    @allure.step('Assert success message is not displayed')
    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *self.success_message_locator
        ), 'Success message is displayed, but should not be'
