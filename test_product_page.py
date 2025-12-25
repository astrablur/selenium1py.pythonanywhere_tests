import pytest

from pages.product_page import ProductPage


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
