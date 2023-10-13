from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep


class SignInPage(Page):
    Email = (By.CSS_SELECTOR, '.input#email-2')
    Password = (By.CSS_SELECTOR, '.input#field')
    Continue = (By.CSS_SELECTOR, '.login-button w-button')
    Email_Input = (By.NAME, 'jacky.hungfai.koo@gmail.com')
    Password_Input = (By.NAME, 'Prius2018!')

    def email_log_in(self):
        self.click(*self.Email)
        sleep(2)

    def password_log_in(self):
        self.click(*self.Password)
        sleep(2)

    def continue_button(self):
        self.click(*self.Continue)
