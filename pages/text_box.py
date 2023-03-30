from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from components.components import WebElement


class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)
        self.pageData = {'title': 'DEMOQA'}
        self.first_line = WebElement(driver, '#userName')
        self.address_line = WebElement(driver, '#currentAddress')
        self.btn_submit = WebElement(driver, '#submit')
        self.bottom_text = WebElement(driver, '#output > div')