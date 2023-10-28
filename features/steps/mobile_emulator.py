from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

@given('Open Login page')
def log_in(context):
    context.app.mobile_page.open_url()

@when('Log in page')
def log_in_page(context):
    sleep(2)
    context.app.sign_in_page.email_log_in()
    context.app.sign_in_page.password_log_in()
    context.app.sign_in_page.continue_button()
    sleep(3)

@when('Click on Free Trial')
def free_sub(context):
    sleep(2)
    context.app.mobile_page.free_trial()
