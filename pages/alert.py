from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from components.components import WebElement
from selenium.webdriver.common.by import By


class Alert(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)
        self.pageData = {'title': 'DEMOQA'}
        self.btn_alert = WebElement(driver, '#alertButton')
        self.btn_confirm = WebElement(driver, '#confirmButton')
        self.confirm_result = WebElement(driver, '#confirmResult')
        self.btn_prompt = WebElement(driver, '#promtButton')
        self.prompt_result = WebElement(driver, '#promptResult')
        self.timer_alert_btn = WebElement(driver, '#timerAlertButton')
