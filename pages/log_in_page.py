from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from support.logger import logger
from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page

class LogInPage(Page):

    Free_Sub = (By.CSS_SELECTOR, '.get-free-period.menu')
    Country_Input = 'USA'
    Your_Country = (By.CSS_SELECTOR, 'input#Your-country')
    Company_Input = 'Myself'
    Company_Name = (By.CSS_SELECTOR, 'input#Company-name-2')
    Name_Input = 'Jacky'
    Your_Name = (By.CSS_SELECTOR, 'input#Director-name')
    Phone_Input = '555-555-5555'
    Your_Phone = (By.CSS_SELECTOR, 'input#Director-phone')
    Email_Input = '123@mail.com'
    Email = (By.CSS_SELECTOR, 'input#Email-2')


    def free_sub(self):
        self.click(*self.Free_Sub)

    def store_original_tab(self):
        return self.get_current_window()

    def switch_to_new_tab(self):
        self.switch_to_new_window()

    def your_country(self):
        self.input_text(self.Country_Input, *self.Your_Country)
        sleep(2)

    def company_name(self):
        self.input_text(self.Company_Input, *self.Company_Name)
        sleep(2)

    def your_name(self):
        self.input_text(self.Name_Input, *self.Your_Name)
        sleep(2)

    def your_phone(self):
        self.input_text(self.Phone_Input, *self.Your_Phone)
        sleep(2)

    def email(self):
        self.input_text(self.Email_Input, *self.Email)
        sleep(2)

    def verify_info(self):
        self.verify_text(*self.Name_Input, *self.Your_Name)
