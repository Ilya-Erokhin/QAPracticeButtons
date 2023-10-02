from selenium.webdriver import Keys
from pages.BasePage import BasePage
from utilities import ConfigReader


class TextInputPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        base_url = ConfigReader.read_configuration('basic info', 'base_url')
        endpoint = "elements/input/simple"
        self.url = f"{base_url}/{endpoint}"

    input_field_id = 'id_text_string'
    submitted_result_with_text_id = 'result'

    def input_text_into_text_field(self, text):
        self.type_into_element('input_field_id', self.input_field_id, text)

    def input_field_is_displayed(self):
        self.display_status('input_field_id', self.input_field_id)

    def submit_via_enter(self):
        input_field = self.get_element('input_field_id', self.input_field_id)
        input_field.send_keys(Keys.RETURN)

    def result_submitted_with_text_displayed(self):
        self.display_status('submitted_result_with_text_id', self.submitted_result_with_text_id)
