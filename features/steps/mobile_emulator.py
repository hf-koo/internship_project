from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

@given('Open Login page')
def log_in(context):
    context.app.mobile_page.open_url_sign_in()