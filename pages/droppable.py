from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from components.components import WebElement
from selenium.webdriver.common.by import By


class DroppAble(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/droppable'
        super().__init__(driver, self.base_url)
        self.pageData = {'title': 'DEMOQA'}
        self.drag = WebElement(driver, '#draggable')
        self.drop = WebElement(driver, '#droppable')
