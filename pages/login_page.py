import allure
from faker import Faker

from pages import BasePage

random_generator = Faker()


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.url = 'https://selenium1py.pythonanywhere.com/accounts/login/'

        self.login_form_locator = ('id', 'login_form')
        self.register_form_locator = ('id', 'register_form')

        self.registration_form_email_input_locator = (
            'id',
            'id_registration-email',
        )
        self.registration_form_password_input_locator = (
            'id',
            'id_registration-password1',
        )
        self.registration_form_confirm_password_input_locator = (
            'id',
            'id_registration-password2',
        )
        self.submit_registration_button_locator = (
            'name',
            'registration_submit',
        )
        self.thanks_for_registration_alert_locator = (
            'css selector',
            '.alert-success',
        )

    @property
    def registration_form_email_input(self):
        return self.find_element(*self.registration_form_email_input_locator)

    @property
    def registration_form_confirm_password_input(self):
        return self.find_element(
            *self.registration_form_confirm_password_input_locator
        )

    @property
    def registration_form_password_input(self):
        return self.find_element(
            *self.registration_form_password_input_locator
        )

    @property
    def submit_registration_button(self):
        return self.find_element(*self.submit_registration_button_locator)

    @allure.step('Register new user')
    def register_new_user(self):
        self.registration_form_email_input.send_keys(random_generator.email())
        password = random_generator.password()
        self.registration_form_password_input.send_keys(password)
        self.registration_form_confirm_password_input.send_keys(password)
        self.submit_registration_button.click()

        self.is_element_present(*self.thanks_for_registration_alert_locator), (
            'Thanks for registration alert should be displayed, '
            'but it is not present'
        )

    @allure.step('Open Login page')
    def open_login_page(self):
        self.open(self.url)

    def should_be_login_form(self):
        assert self.is_element_present(
            *self.login_form_locator
        ), 'Login form is not present, but should be'

    @allure.step(
        'Assert page contains login url, login form and register form'
    )
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert (
            'login' in self.browser.current_url
        ), 'Current url is not equal to Login page url'

    def should_be_register_form(self):
        assert self.is_element_present(
            *self.register_form_locator
        ), 'Register form is not present, but should be'
