from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException


class WebElement:
    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator

    def click(self):
        self.find_element().click()

    def find_element(self):
        time.sleep(3)
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def find_elements(self):
        time.sleep(3)
        return self.driver.find_elements(By.CSS_SELECTOR, self.locator)

    def check_count_elements(self, count: int):
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





