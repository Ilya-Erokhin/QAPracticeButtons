from behave import *

from pages.HomePage import HomePage
from pages.SimpleButtonPage import SimpleButtonPage


@given('I navigate to the Home Page')
def step_impl(context):
    context.home_page = HomePage(context.driver)

@when('I click on Simple Page button')
def step_impl(context):
    home_page = HomePage(context.driver)
    home_page.select_simple_button_page()

@when('I click on "Click" button')
def step_impl(context):
    context.simple_button_page = SimpleButtonPage(context.driver)
    context.simple_button_page.click_on_click_on_simple_button()

@then('I can see the Submitted result')
def step_impl(context):
    context.simple_button_page = SimpleButtonPage(context.driver)
    context.simple_button_page.result_submitted_displayed()