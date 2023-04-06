from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from components.components import WebElement
from selenium.webdriver.common.by import By


class ProgressBar(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/progress-bar'
        super().__init__(driver, self.base_url)
        self.pageData = {'title': 'DEMOQA'}
        self.start_btn = WebElement(driver, '#startStopButton')
        self.progress_bar = WebElement(driver, '#progressBar > div')