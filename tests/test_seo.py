from pages.demoqa import DemoQa
from pages.accordion import Accordion
from pages.alert import Alert
from pages.browser_tab import BrowserTab
import pytest
import time


def test_check_title_demo(browser):

    demo_page_1 = DemoQa(browser)
    demo_page_1.visit()
    assert browser.title == demo_page_1.pageData['title']


#!!!!! NB: VERY IMPORTANT TEST CASE!!!
@pytest.mark.parametrize("pages", [DemoQa, Accordion, Alert, BrowserTab])
    #1- 1 arguement\переменная ""
    #2 список значений []
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert browser.title == page.pageData['title']  #compare with title specified in pageClass

