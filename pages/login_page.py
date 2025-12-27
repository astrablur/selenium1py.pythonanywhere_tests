from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.browser.find_element(
            *LoginPageLocators.REGISTRATION_FORM_EMAIL_INPUT
        ).send_keys(email)
        self.browser.find_element(
            *LoginPageLocators.REGISTRATION_FORM_PASSWORD_INPUT
        ).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.REGISTRATION_FORM_CONFIRM_PASSWORD_INPUT
        ).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.SUBMIT_REGISTRATION_BUTTON
        ).click()

        self.is_element_present(
            *LoginPageLocators.THANKS_FOR_REGISTRATION_ALERT
        ), (
            'Thanks for registration alert should be displayed, '
            'but it is not present'
        )

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), 'Login form is not present'

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Login url is not found'

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM
        ), 'Register form is not present'
