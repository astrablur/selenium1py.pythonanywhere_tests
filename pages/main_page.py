from .base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element('id', 'login_link')
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(
            'id', 'login_link'
        ), 'Login link is not presented'
