import pytest

from pages.login_page import LoginPage
from pages.product_page import ProductPage


def test_guest_should_see_login_link_on_product_page(browser):
    link = (
        'https://selenium1py.pythonanywhere.com/catalogue/'
        'the-city-and-the-stars_95/'
    )
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = (
        'https://selenium1py.pythonanywhere.com/catalogue/'
        'test-driven-development_124/'
    )
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.parametrize(
    'num',
    [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9],
)
def test_guest_can_add_product_to_basket(num, browser):
    link = (
        f'https://selenium1py.pythonanywhere.com/catalogue/'
        f'coders-at-work_207/?promo=offer{num}'
    )
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.assert_basket_messages()


@pytest.mark.xfail(reason='negative test')
def test_guest_cant_see_success_message_after_adding_product_to_basket(
    browser,
):
    link = (
        'https://selenium1py.pythonanywhere.com/catalogue/'
        'learning-python_121/'
    )
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_button()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = (
        'https://selenium1py.pythonanywhere.com/'
        'catalogue/the-clean-coder_150/'
    )
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason='negative test')
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/freedom_24/'
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_button()
    page.assert_success_message_disappeared()
