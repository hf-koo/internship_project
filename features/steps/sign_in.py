from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

Email = (By.ID, '#email-2')
Password = (By.ID, '#field')
Continue = (By.CSS_SELECTOR, '.login-button w-button')

@given('Open Main page')
def open_reelly(context):
    context.driver.get('https://soft.reelly.io/')

@when('Log in to the page')
def log_in_page(context):
    context.driver.find_element(*Email)
    sleep(2)
    context.driver.find_element(*Password)
    sleep(2)
    context.driver.find_element(*Continue).click()