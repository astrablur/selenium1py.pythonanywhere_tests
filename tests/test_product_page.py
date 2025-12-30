import allure
import pytest


@pytest.mark.product_page
@pytest.mark.regression
class TestProductPage:

    @allure.feature('Product page')
    @allure.story('Login from Product page')
    @allure.title('Guest should see login link on Product page')
    @pytest.mark.guest
    @pytest.mark.smoke
    def test_guest_should_see_login_link_on_product_page(self, product_page):
        link = (
            'https://selenium1py.pythonanywhere.com/catalogue/'
            'the-city-and-the-stars_95/'
        )
        product_page.open_product_page(link)
        product_page.should_be_login_link()

    @allure.feature('Product page')
    @allure.story('Login from Product page')
    @allure.title('Guest can go to login page from Main page')
    @pytest.mark.guest
    @pytest.mark.smoke
    def test_guest_can_go_to_login_page_from_product_page(
        self, product_page, login_page
    ):
        link = (
            'https://selenium1py.pythonanywhere.com/catalogue/'
            'test-driven-development_124/'
        )
        product_page.open_product_page(link)
        product_page.go_to_login_page()
        login_page.should_be_login_page()

    @allure.feature('Product page')
    @allure.story('Adding product to basket')
    @allure.title('Guest see no messages on Product page')
    @pytest.mark.basket
    @pytest.mark.guest
    def test_guest_should_not_see_success_basket_message(self, product_page):
        link = (
            'https://selenium1py.pythonanywhere.com/'
            'catalogue/the-clean-coder_150/'
        )
        product_page.open_product_page(link)
        product_page.should_not_be_success_message()

    @allure.feature('Product page')
    @allure.story('Adding product to basket')
    @allure.title('Authorized user see no messages on Product page')
    @pytest.mark.basket
    @pytest.mark.user
    def test_user_should_not_see_success_basket_message(
        self, authorized_user, product_page
    ):
        link = (
            'https://selenium1py.pythonanywhere.com/'
            'catalogue/the-clean-coder_150/'
        )
        product_page.open_product_page(link)
        product_page.should_not_be_success_message()

    @allure.feature('Product page')
    @allure.story('Adding product to basket')
    @allure.title('Add to basket button is present on Product page')
    @pytest.mark.basket
    @pytest.mark.smoke
    def test_add_to_basket_button_is_present_on_product_page(
        self, product_page
    ):
        link = (
            f'https://selenium1py.pythonanywhere.com/catalogue/'
            f'coders-at-work_207/'
        )
        product_page.open_product_page(link)
        product_page.assert_add_to_basket_button_is_present_and_active()

    @allure.feature('Product page')
    @allure.story('Adding product to basket')
    @allure.title('Guest can add product to basket')
    @pytest.mark.basket
    @pytest.mark.guest
    @pytest.mark.smoke
    @pytest.mark.parametrize(
        'num',
        [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9],
    )
    def test_guest_can_add_product_to_basket(self, num, product_page):
        link = (
            f'https://selenium1py.pythonanywhere.com/catalogue/'
            f'coders-at-work_207/?promo=offer{num}'
        )
        product_page.open_product_page(link)
        product_page.click_add_to_basket_button()
        product_page.solve_quiz_and_get_code()
        product_page.assert_basket_messages()

    @allure.feature('Product page')
    @allure.story('Adding product to basket')
    @allure.title('User can add product to basket')
    @pytest.mark.basket
    @pytest.mark.user
    @pytest.mark.smoke
    def test_user_can_add_product_to_basket(
        self, authorized_user, product_page
    ):
        link = (
            'https://selenium1py.pythonanywhere.com/catalogue/'
            'coders-at-work_207/'
        )
        product_page.open_product_page(link)
        product_page.click_add_to_basket_button()
        product_page.assert_basket_messages()

    @allure.feature('Product page')
    @allure.story('Empty basket from Product page')
    @allure.title(
        'Guest see no products in empty basket opened from Product page'
    )
    @pytest.mark.basket
    @pytest.mark.guest
    def test_guest_see_no_products_in_empty_basket_opened_from_product_page(
        self, product_page, basket_page
    ):
        link = (
            'https://selenium1py.pythonanywhere.com/catalogue/'
            'sams-teach-yourself-mysql-in-24-hours_145/'
        )
        product_page.open_product_page(link)
        product_page.click_view_basket_link()
        basket_page.assert_basket_has_no_products()
        basket_page.assert_basket_empty_message()
