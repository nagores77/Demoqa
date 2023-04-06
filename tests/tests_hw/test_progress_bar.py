from pages.progress_bar import ProgressBar
import time
import pytest
import allure
from selenium.webdriver import ActionChains

@allure.title('Проверка progress bar')
#@pytest.mark.xfail(condition=True, reason='Если страница недоступна, тест будет помечен, как xfail')
def test_check_progress_bar(browser):

    demo_page = ProgressBar(browser)
    demo_page.visit()
    action_chains = ActionChains(browser)
    time.sleep(2)

    demo_page.start_btn.click()

    if demo_page.progress_bar.check_css('width', '51%'):
        demo_page.start_btn.click()

    assert demo_page.progress_bar.check_css('width', '51%')

    #assert demo_page.progress_bar.check_css('width', '25%')


