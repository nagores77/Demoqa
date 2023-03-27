from pages.base_page import BasePage
from components.components


class Accordion(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)
        self.text_block = WebElements(driver, '#section1Content > p ')
