from pages.demoqa import DemoQa
from pages.elements_page import ElementPage


def test_go_to_page_elements(browser):

    demo_page = DemoQa(browser)
    demo_element = ElementPage(browser)

    demo_page.visit()
    assert demo_page.equal_url()
    demo_page.click_on_the_btn_elements()
    assert demo_element.equal_url()


