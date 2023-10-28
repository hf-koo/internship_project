from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep


class MobilePage(Page):

    Free_Trial = (By.CSS_SELECTOR, 'a[wized="freeUserMobileMenu"][href="/book-presentation"]')

    def log_in(self):
        self.open_url_sign_in()

    def free_trial(self):
        self.click(*self.Free_Trial)