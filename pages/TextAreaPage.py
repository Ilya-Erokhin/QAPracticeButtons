from selenium.webdriver import Keys
from pages.BasePage import BasePage
from utilities import ConfigReader


class TextAreaPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        base_url = ConfigReader.read_configuration('basic info', 'base_url')
        endpoint = "elements/textarea/single"
        self.url = f"{base_url}/{endpoint}"
