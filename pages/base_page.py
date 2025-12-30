import math

import allure
from selenium.common import (
    NoSuchElementException,
    NoAlertPresentException,
    TimeoutException,
)
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.url = 'https://selenium1py.pythonanywhere.com/'

        self.wait = WebDriverWait(self.browser, 5)
        self.ec = ec

        self.login_link_locator = ('id', 'login_link')
        self.view_basket_link_locator = ('css selector', '.basket-mini a')
        self.user_icon_locator = ('class name', 'icon-user')

    @property
    def login_link(self):
        return self.find_element(*self.login_link_locator)

    @property
    def view_basket_link(self):
        return self.find_element(*self.view_basket_link_locator)

    @allure.step('Click View basket link')
    def click_view_basket_link(self):
        self.view_basket_link.click()

    def find_element(self, how, what):
        return self.browser.find_element(how, what)

    @allure.step('Click link to Login page')
    def go_to_login_page(self):
        self.login_link.click()

    def is_element_present(self, how, what):
        try:
            self.wait.until(self.ec.presence_of_element_located((how, what)))
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what):
        try:
            self.wait.until(self.ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def open(self, url):
        self.browser.get(url)

    @allure.step('Assert authenticated user icon is displayed')
    def should_be_authorized_user(self):
        assert self.is_element_present(
            *self.user_icon_locator
        ), 'User icon is not displayed, probably unauthorised user'

    @allure.step('Assert page contains link to Login page')
    def should_be_login_link(self):
        assert self.is_element_present(
            *self.login_link_locator
        ), 'Login link is not displayed, but should be'

    @allure.step('Solve quiz and get code for alert')
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert

        number = alert.text.split('\n', 1)[0].split('=')[1].strip()
        answer = str(math.log(abs((12 * math.sin(float(number))))))

        alert.send_keys(answer)
        alert.accept()

        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f'Your code: {alert_text}')
            alert.accept()
        except NoAlertPresentException:
            print('No second alert presented')
