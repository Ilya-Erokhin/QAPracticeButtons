from behave import *
from pages.SimpleButtonPage import SimpleButtonPage


@given('I navigate into the Simple Button Page')
def step_impl(context):
    context.simple_button_page = SimpleButtonPage(context.driver)
    context.driver.get(context.simple_button_page.url)

@when('I click on "Click" button')
def step_impl(context):
    context.simple_button_page = SimpleButtonPage(context.driver)
    context.simple_button_page.click_on_click_on_simple_button()

@then('I can see the Submitted result')
def step_impl(context):
    context.simple_button_page = SimpleButtonPage(context.driver)
    context.simple_button_page.result_submitted_displayed()