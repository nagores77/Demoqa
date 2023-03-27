from pages.demoqa import DemoQa
from selenium.webdriver.common.by import By
from pages.elements_page import ElementsPage


def get_text(browser):

    demo_page = DemoQa(browser)

    demo_page.visit()

    assert demo_page.driver.get_text == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

    demo_page.btn_elements.click()

    assert demo_page.driver.get_text() == 'Please select an item from left to start practice.'


def test_page_elements(browser):

    elements_page = ElementsPage(browser)

    elements_page.visit()

    assert elements_page.new_element.get_text() == 'Elements'
    assert elements_page.icon.exist()
    assert elements_page.btn_sidebar_first.exist()
    assert elements_page.btn_sidebar_first_textbox.exist()



