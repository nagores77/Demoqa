from pages.demoqa import DemoQa
import time


def test_window_size(browser):

    demo_page_1 = DemoQa(browser)
    demo_page_1.visit()
    browser.set_window_size(1000, 300)
    time.sleep(2)
    browser.set_window_size(1000, 1000)