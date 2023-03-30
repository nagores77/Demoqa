from pages.modal_dialogs import ModalDialogs
from pages.demoqa import DemoQa
from pages.base_page import BasePage


def test_modal_elements(browser):

    demo_page = ModalDialogs(browser)
    demo_page.visit()
    assert demo_page.element_group.check_count_elements(count=6)



def test_navigation_modal(browser):
    demo_page1 = ModalDialogs(browser)
    basic_page = DemoQa(browser)

    demo_page1.visit()
    browser.refresh()
    demo_page1.main_icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    basic_page.equal_url()
    # assert demo_page1.get_url() == 'https://demoqa.com/'
    assert browser.title == demo_page1.pageData['title']
    browser.set_window_size(1000, 1000)
