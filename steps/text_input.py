from behave import *
from pages.TextInputPage import TextInputPage


@given('I navigate into the Text Input Page')
def step_impl(context):
    context.text_input_page = TextInputPage(context.driver)
    context.driver.get(context.text_input_page.url)


@when('I can see the Input Field')
def step_impl(context):
    context.text_input_page = TextInputPage(context.driver)
    context.text_input_page.input_field_is_displayed()


@when('I type "{text}" into the field')
def step_impl(context, text):
    context.text_input_page = TextInputPage(context.driver)
    context.text_input_page.input_text_into_text_field(text)


@when('Submit the result via Enter')
def step_impl(context):
    context.text_input_page = TextInputPage(context.driver)
    context.text_input_page.submit_via_enter()


@then('I can see the Submitted result with my text')
def step_impl(context):
    context.text_input_page = TextInputPage(context.driver)
    context.text_input_page.result_submitted_with_text_displayed()
