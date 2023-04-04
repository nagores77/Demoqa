from pages.browser_tab import BrowserTab
import allure
import time


@allure.title('Browser Tab')
def test_browser_tab(browser):
    demo_page = BrowserTab(browser)
    demo_page.visit()

    assert len(browser.window_handles) == 1
    assert demo_page.get_url() == 'https://demoqa.com/browser-windows'

    demo_page.new_tab.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2


    browser.switch_to.window(browser.window_handles[0])
    time.sleep(2)
    assert demo_page.get_url() == 'https://demoqa.com/browser-windows'


