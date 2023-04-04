from pages.webtables import WebTables
import time
import pytest
import allure

@allure.title('Проверка таймера алерта')
#@pytest.mark.xfail(condition=True, reason='Если страница недоступна, тест будет помечен, как xfail')
def test_check_modal(browser):

    demo_page = WebTables(browser)
    demo_page.visit()
