from pages.links import Links
import time
import pytest
import allure

@allure.title('Проверка таймера алерта')
#@pytest.mark.xfail(condition=True, reason='Если страница недоступна, тест будет помечен, как xfail')
def test_check_modal(browser):

    demo_page = Links(browser)
    demo_page.visit()

    assert demo_page.home_link.exist()
    assert demo_page.home_link.get_text() == 'Home'
    assert demo_page.home_link.get_dom_attribute('href') == 'https://demoqa.com'
    demo_page.home_link.click()








