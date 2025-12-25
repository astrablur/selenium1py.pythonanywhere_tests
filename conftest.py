import pytest
from selenium import webdriver


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

    user_language = request.config.getoption('--language')
    driver_options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language}
    )

    driver = webdriver.Chrome(options=driver_options)
    driver.user_language = user_language
    yield driver

    print('\nQuit browser')
    driver.quit()
