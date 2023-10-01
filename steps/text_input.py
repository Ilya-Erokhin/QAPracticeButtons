from behave import *
from selenium.webdriver import Keys

from pages.HomePage import HomePage
from pages.TextInputPage import TextInputPage


@when('I click on Input Simple Page button')
def step_impl(context):
    home_page = HomePage(context.driver)
    home_page.select_text_input_page()

@when('I can see the Input Field')
def step_impl(context):
    text_input_page = TextInputPage(context.driver)
    text_input_page.input_field_is_displayed()

@when('I type "{text}" into the field')
def step_impl(context, text):
    text_input_page = TextInputPage(context.driver)
    text_input_page.input_text_into_text_field(text)

@when('Submit the result via Enter')
def step_impl(context):
    text_input_page = TextInputPage(context.driver)
    text_input_page.submit_via_enter()

@then('I can see the Submitted result with my text')
def step_impl(context):
    context.text_input_page = TextInputPage(context.driver)
    context.text_input_page.result_submitted_with_text_displayed()
