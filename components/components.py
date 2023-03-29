from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class WebElement:
    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator

    def click(self):
        self.find_element().click()

    def click_force(self):
        self.driver.execute_script('arguments[0].click();', self.find_element())

    def find_element(self):
        time.sleep(3)
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def find_elements(self):
        time.sleep(3)
        return self.driver.find_elements(By.CSS_SELECTOR, self.locator)

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






