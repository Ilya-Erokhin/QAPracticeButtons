from behave import *

from pages.HomePage import HomePage


@given('I navigate into the Home Page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.driver.get(context.home_page.base_url)

@then('I can see Text Input button')
def step_impl(context):
    context.home_page = context.home_page = HomePage(context.driver)
    context.home_page.text_input_button_is_displayed()
