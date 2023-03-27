
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from components.components import WebElement


class FormPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)
        self.pageData = {'title': 'DEMOQA'}
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        #self.e_mail = WebElement(driver, '#userEmail')
        self.gender = WebElement(driver, '#gender-radio-2')
        self.mobile = WebElement(driver, '#userNumber')



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





