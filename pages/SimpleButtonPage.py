from pages.BasePage import BasePage
from utilities import ConfigReader


class SimpleButtonPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        base_url = ConfigReader.read_configuration('basic info', 'base_url')
        endpoint = "elements/button/simple"
        self.url = f"{base_url}/{endpoint}"

    button_click_selector_id = 'submit-id-submit'
    button_simple_button_text_selector_class_name = 'tab active'
    submitted_result_selector_id = 'result-text'
    requirements_selector_id = 'req_header'
    contact_selector_link_text = 'Contact'
    whats_new_selector_link_text = "What's new"

    def click_on_click_on_simple_button(self):
        self.click_on_element('button_click_selector_id', self.button_click_selector_id)

    def click_on_simple_button_text(self):
        self.click_on_element('button_simple_button_text_selector_class_name', self.button_simple_button_text_selector_class_name)

    def result_submitted_displayed(self):
        self.display_status('submitted_result_selector_id', self.submitted_result_selector_id)

    def click_on_requirements(self):
        self.click_on_element('requirements_selector_id', self.requirements_selector_id)

    def click_on_contact_button(self):
        self.click_on_element('contact_selector_link_text', self.contact_selector_link_text)

    def click_on_whats_new_button(self):
        self.click_on_element('whats_new_selector_link_text', self.whats_new_selector_link_text)
