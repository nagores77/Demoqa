from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from components.components import WebElement


class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)
        self.pageData = {'title': 'DEMOQA'}
        self.element_group = WebElement(driver, '#app > div > div > div.row > div:nth-child(1) > div > div > div')
        self.main_icon = WebElement(driver, '#app > header > a > img')