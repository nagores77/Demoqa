from pages.demoqa import DemoQa
from selenium.webdriver.common.by import By


def get_text(browser):

    demo_page = DemoQa(browser)

    demo_page.visit()
    demo_page.driver.find_element(By.CSS_SELECTOR, '#app > footer > span')

    assert demo_page.driver.find_element == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

    demo_page.btn_elements.click()
    demo_page.driver.find_element(By.CSS_SELECTOR, '#app div.row > div.col-12.mt-4.col-md-6')
    assert demo_page.driver.find_element == 'Please select an item from left to start practice.'
