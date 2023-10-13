from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from support.logger import logger
from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page

class LogInPage(Page):

    Free_Sub = (By.CSS_SELECTOR, '.get-free-period.menu')
    def free_sub(self):
        self.click(*self.Free_Sub)




