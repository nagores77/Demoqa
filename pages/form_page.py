
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from components.components import WebElement
from selenium.webdriver.common.by import By


class FormPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)
        self.pageData = {'title': 'DEMOQA'}
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.gender_radio_2 = WebElement(driver, '#gender-radio-2')
        self.user_number = WebElement(driver, '#userNumber')
        self.btn_submit = WebElement(driver, '#submit')
        self.modal_dialog = WebElement(driver, 'body > div.fade.modal.show > div')
        self.btn_close_modal = WebElement(driver, '#closeLargeModal')
        self.form_validation = WebElement(driver, '#userForm')

        self.btn_state_menu = WebElement(driver, '#state > div:nth-child(1) > div:nth-child(2) > div:nth-child(2)')
        self.state_list = WebElement(driver, '#react-select-3-input')

        self.btn_city_menu = WebElement(driver, '#city > div > div.css-1wy0on6 > div')
        self.city_list = WebElement(driver, '#react-select-4-input')







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





