from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from components.components import WebElement
from selenium.webdriver.common.by import By


class Slider(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/slider'
        super().__init__(driver, self.base_url)
        self.pageData = {'title': 'DEMOQA'}
        self.slider_container = WebElement(driver, '#sliderContainer')
        #self.slider_value = WebElement(driver, '#sliderValue')
        self.slider_value = WebElement(driver, '#sliderContainer > div.col-9 > span > input')


        # sliderContainer > div.col-9 > span > div > div.range-slider__tooltip__label
        # sliderContainer > div.col-9 > span > div > div.range-slider__tooltip__arrow

