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
def free_trial(context):
    sleep(2)
    context.app.mobile_page.free_trial()

@when('Find Free Sub')
def free_sub(context):
    context.app.mobile_page.free_sub()

@when('Enter texts information in the form')
def enter_text(context):
    context.app.log_in_page.your_country()
    context.app.log_in_page.company_name()
    context.app.log_in_page.your_name()
    context.app.log_in_page.your_phone()
    context.app.log_in_page.email()

@then('verify info is correct')
def verify_correct_info(context):
    context.app.log_in_page.verify_info()

@then('Verify application btn is available')
def application_btn(context):
    context.app.log_in_page.send_application_button()