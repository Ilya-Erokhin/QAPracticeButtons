from pages.BasePage import BasePage
from pages.SimpleButtonPage import SimpleButtonPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    simple_button_on_start_link_text = 'Simple button'

    def select_simple_button_page(self):
        self.click_on_element('simple_button_on_start_link_text', self.simple_button_on_start_link_text)
        return SimpleButtonPage(self.driver)
