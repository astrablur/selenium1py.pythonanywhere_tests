from pathlib import Path

import pytest
from selenium import webdriver

from pages import MainPage, LoginPage, BasketPage, ProductPage


def pytest_configure(config):
    current_file = Path(__file__).resolve()
    allure_dir = current_file.parents[1] / 'allure-results'
    allure_dir.mkdir(exist_ok=True)
    config.option.allure_report_dir = str(allure_dir)


def pytest_addoption(parser):
    parser.addoption(
        '--language',
        action='store',
        default='en',
        help='Choose language: ',
        # fmt: off
        choices=('ar', 'ca', 'cs', 'da', 'de', 'en', 'el',
                 'es', 'fi', 'fr', 'it', 'ko', 'nl', 'pl',
                 'pt', 'pt-br', 'ro', 'ru', 'sk', 'uk', 'zh-hans')
        # fmt: on
    )


@pytest.fixture()
def browser(request):
    print('\nStart browser for test')

    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    driver_options.add_argument('--window-size=1920,1080')
    driver_options.add_argument('--headless=new')

    user_language = request.config.getoption('--language')
    driver_options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language}
    )

    driver = webdriver.Chrome(options=driver_options)
    yield driver

    print('\nQuit browser')
    driver.quit()


@pytest.fixture()
def main_page(browser):
    return MainPage(browser)


@pytest.fixture()
def login_page(browser):
    return LoginPage(browser)


@pytest.fixture()
def authorized_user(browser, login_page):
    login_page.open_login_page()
    login_page.register_new_user()
    login_page.should_be_authorized_user()


@pytest.fixture()
def basket_page(browser):
    return BasketPage(browser)


@pytest.fixture()
def product_page(browser):
    return ProductPage(browser)
