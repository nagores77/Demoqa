
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from components.components import WebElement


class DemoQa(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)
        self.icon = WebElement(driver, '#app > header >a')
        self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')


    #def test_icon_exist(self):
     #   try:
      ## except NoSuchElementException:
        #    return False
        #return True

    # def click_on_the_icon(self):
    #     return self.find_element(locator='#app > header >a').click()

    #def equal_url(self):
        #if self.get_url == self.base_url:
            #return True
        #return False

    # def click_on_the_btn_elements(self):
    #     return self.find_element(locator='#app > div > div > div.home-body > div > div:nth-child(1)').click





