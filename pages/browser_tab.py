from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from components.components import WebElement
from selenium.webdriver.common.by import By


class BrowserTab(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/browser-windows'
        super().__init__(driver, self.base_url)

        self.new_tab = WebElement(driver, '#tabButton')