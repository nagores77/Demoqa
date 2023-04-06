from pages.slider import Slider
import time
import pytest
import allure
from selenium.webdriver import ActionChains

@allure.title('Проверка slider')
#@pytest.mark.xfail(condition=True, reason='Если страница недоступна, тест будет помечен, как xfail')
def test_check_slider(browser):

    demo_page = Slider(browser)
    demo_page.visit()
    action_chains = ActionChains(browser)

    assert demo_page.slider_container.exist()
    #assert demo_page.slider_value.get_text() == 25
    assert demo_page.slider_value.check_css('value', '25')

    #demo_page.slider_container.

    #assert demo_page.slider_container.get_dom_attribute('style') == "--value:25"

    #assert demo_page.slider_value.get_text() == 25

    action_chains.drag_and_drop_by_offset(demo_page.slider_container.find_element(), -58, 0).perform()
    time.sleep(5)
    assert demo_page.slider_value.check_css('value', '50')
