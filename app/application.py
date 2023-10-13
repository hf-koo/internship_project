from pages.main_page import MainPage
from pages.sign_in_page import SignInPage
from pages.base_page import Page
from pages.log_in_page import LogInPage

class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.log_in_page = LogInPage(driver)
