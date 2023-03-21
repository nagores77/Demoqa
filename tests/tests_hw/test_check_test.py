from pages.demoqa import DemoQa
from selenium.webdriver.common.by import By


def get_text(browser):

    demo_page = DemoQa(browser)

    demo_page.visit()
    demo_page.driver.find_element(By.CSS_SELECTOR, '#app > footer > span')

    assert demo_page.driver.find_element == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
