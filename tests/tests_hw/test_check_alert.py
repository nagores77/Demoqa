from pages.alert import Alert
import time
import pytest
import allure

@allure.title('Проверка таймера алерта')
#@pytest.mark.xfail(condition=True, reason='Если страница недоступна, тест будет помечен, как xfail')
def test_check_modal(browser):

    demo_page = Alert(browser)
    demo_page.visit()

    assert demo_page.timer_alert_btn.exist()

    start = time.time()
    demo_page.timer_alert_btn.click()
    if time.time() == start + 5:
        assert demo_page.alert()

        time.sleep(10)




