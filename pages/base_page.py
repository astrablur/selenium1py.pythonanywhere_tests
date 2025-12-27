import math

from selenium.common import (
    NoSuchElementException,
    NoAlertPresentException,
    TimeoutException,
)
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def click_checkout_basket_link(self):
        self.browser.find_element(
            *BasePageLocators.CHECKOUT_BASKET_LINK
        ).click()

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1).until_not(
                ec.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False

        return True

    def is_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                ec.presence_of_element_located((how, what))
            )
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                ec.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return True

        return False

    def open(self):
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        assert self.is_element_present(
            *BasePageLocators.USER_ICON
        ), 'User icon is not presented, probably unauthorised user'

    def should_be_login_link(self):
        assert self.is_element_present(
            *BasePageLocators.LOGIN_LINK
        ), 'Login link is not presented'

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
