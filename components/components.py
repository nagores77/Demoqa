from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import logging


class WebElement:
    def __init__(self, driver, locator='', locator_type='css'):
        self.driver = driver
        self.locator = locator
        self.locator_type = locator_type

    def click(self):
        self.find_element().click()

    def click_force(self):
        self.driver.execute_script('arguments[0].click();', self.find_element())

    def find_element(self):
        time.sleep(3)
        return self.driver.find_element(self.get_by_type(), self.locator)

    def find_elements(self):
        time.sleep(3)
        return self.driver.find_elements(self.get_by_type(), self.locator)

    def check_count_elements(self, count: int) -> bool:
        if len(self.find_elements()) == count:
            return True
        return False

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def get_text(self):
        return str(self.find_element().text)

    def test_icon_exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def visible(self):
        return self.find_element().is_displayed()

    def send_keys(self, text: str):
        self.find_element().send_keys(text)

    def clear(self):
        self.find_element().send_keys(Keys.CONTROL + 'a')  # можно сделать так: self.send_keys(Keys.CONTROL + 'a')
        self.find_element().send_keys(Keys.DELETE)

    def get_dom_attribute(self, name: str):
        value = self.find_element().get_dom_attribute(name)

        if value is None:
            return False
        if len(value) > 0:
            return value
        return True

    def arrow_down(self):
        self.find_element().send_keys(Keys.ARROW_DOWN)
        self.find_element().send_keys(Keys.ENTER)

    def get_by_type(self):
        if self.locator_type == 'id':
            return By.ID
        elif self.locator_type == 'name':
            return By.NAME
        elif self.locator_type == 'xpath':
            return By.XPATH
        elif self.locator_type == 'css':
            return By.CSS_SELECTOR
        elif self.locator_type == 'class':
            return By.CLASS_NAME
        elif self.locator_type == 'link':
            return By.LINK_TEXT
        else:
            print('locator type' + self.locator_type + 'not correct')
            return False

    def scroll_to_element(self):
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);', self.find_element())

    def check_css(self, style, value=''):   #посылаем стиль и значание конкретного эл-та
        try:
            self.driver.execute_script(f"arguments[0].style.{style} = '{value}';", self.find_element())
        except Exception as ex:
            logging.log(1, ex)
            return False
        return True





