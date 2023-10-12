from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    Email = (By.ID, '#email-2')
    Password = (By.ID, '#field')
    Continue = (By.CSS_SELECTOR, '.login-button w-button')

    def verify_signin_opened(self, expected_result):
        self.verify_text(expected_result, *self.SIGNIN_HEADER)