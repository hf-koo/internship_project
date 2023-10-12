from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


@given('Open Main page')
def open_reelly(context):
    context.app.main_page.open_main()

# @when('Log in to the page')
# def log_in_page(context):
