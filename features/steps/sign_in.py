from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


@given('Open Main page')
def open_reelly(context):
    context.app.main_page.open_main()

@when('Log in to the page')
def log_in_page(context):
    sleep(2)
    context.app.sign_in_page.email_log_in()
    context.app.sign_in_page.password_log_in()
    context.app.sign_in_page.continue_button()
    sleep(3)

@when('Click on Get a free Subscription')
def free_sub(context):
    context.app.log_in_page.free_sub()

@when('Switch the new tab')
def switch_to_new_tab(context):
    context.app.log_in_page.switch_to_new_tab()

@when('Enter some test information in the form at the right side of the page')
def enter_some_test(context):
    context.app.log_in_page.your_country()
    context.app.log_in_page.company_name()
    context.app.log_in_page.your_name()
    context.app.log_in_page.your_phone()
    context.app.log_in_page.email()

@then('Verify the right information is present')
def verify_right_information(context):
    context.app.log_in_page.verify_info()

@then('Verify send an application button is available')
def send_application_btn(context):
    context.app.log_in_page.send_application_button()

