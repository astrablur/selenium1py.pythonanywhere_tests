import time

import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


def test_guest_should_see_login_link_on_product_page(browser):
    link = (
        'https://selenium1py.pythonanywhere.com/catalogue/'
        'the-city-and-the-stars_95/'
    )
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = (
        'https://selenium1py.pythonanywhere.com/catalogue/'
        'test-driven-development_124/'
    )
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_success_message(browser):
    link = (
        'https://selenium1py.pythonanywhere.com/'
        'catalogue/the-clean-coder_150/'
    )
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()


def test_add_to_basket_button_is_present_on_product_page(browser):
    link = (
        f'https://selenium1py.pythonanywhere.com/catalogue/'
        f'coders-at-work_207/'
    )
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.assert_add_to_basket_button_is_present_and_active()


@pytest.mark.need_review
@pytest.mark.parametrize(
    'num',
    [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9],
)
def test_guest_can_add_product_to_basket(num, browser):
    link = (
        f'https://selenium1py.pythonanywhere.com/catalogue/'
        f'coders-at-work_207/?promo=offer{num}'
    )
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_add_to_basket_button()
    product_page.solve_quiz_and_get_code()
    product_page.assert_basket_messages()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = (
        'https://selenium1py.pythonanywhere.com/catalogue/'
        'sams-teach-yourself-mysql-in-24-hours_145/'
    )
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_checkout_basket_link()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.assert_basket_has_no_products()
    basket_page.assert_basket_empty_message()


@pytest.mark.xfail(reason='negative test')
def test_guest_cant_see_success_message_after_adding_product_to_basket(
    browser,
):
    link = (
        'https://selenium1py.pythonanywhere.com/catalogue/'
        'learning-python_121/'
    )
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_add_to_basket_button()
    product_page.should_not_be_success_message()


@pytest.mark.xfail(reason='negative test')
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/freedom_24/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_add_to_basket_button()
    product_page.assert_success_message_disappeared()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        link = 'https://selenium1py.pythonanywhere.com/accounts/login/'
        login_page = LoginPage(browser, link)
        login_page.open()

        user_email = str(time.time()) + '@fakemail.org'
        user_password = 'SeleniumPythonAutomation2025'
        login_page.register_new_user(user_email, user_password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = (
            'https://selenium1py.pythonanywhere.com/'
            'catalogue/the-clean-coder_150/'
        )
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = (
            'https://selenium1py.pythonanywhere.com/catalogue/'
            'coders-at-work_207/'
        )
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.click_add_to_basket_button()
        product_page.assert_basket_messages()
