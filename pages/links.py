from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from components.components import WebElement
from selenium.webdriver.common.by import By


class Links(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/links'
        super().__init__(driver, self.base_url)
        self.pageData = {'title': 'DEMOQA'}

        self.home_link = WebElement(driver, '#simpleLink')



