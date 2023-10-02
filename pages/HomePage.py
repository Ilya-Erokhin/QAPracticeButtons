from pages.BasePage import BasePage
from pages.SimpleButtonPage import SimpleButtonPage
from utilities import ConfigReader


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = ConfigReader.read_configuration('basic info', 'base_url')

    text_input_link_text = 'Text input'
    simple_button_on_start_link_text = 'Simple button'

    def select_text_input_page(self):
        self.click_on_element('text_input_link_text', self.text_input_link_text)

    def select_simple_button_page(self):
        self.click_on_element('simple_button_on_start_link_text', self.simple_button_on_start_link_text)
        return SimpleButtonPage(self.driver)

    def text_input_button_is_displayed(self):
        self.display_status('text_input_link_text', self.text_input_link_text)
