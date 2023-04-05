from pages.demoqa import DemoQa
from pages.accordion import Accordion
from pages.alert import Alert
from pages.browser_tab import BrowserTab
from pages.base_page import BasePage
import pytest
import time

@pytest.mark.parametrize("pages", [DemoQa, Accordion, Alert, BrowserTab])
    #1- 1 arguement\переменная ""
    #2 список значений []
def test_seo_meta(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)

    assert page.meta_teg.exist()
    assert page.meta_teg.get_dom_attribute('name') == "viewport"
    assert page.meta_teg.get_dom_attribute('content') == "width=device-width,initial-scale=1"
