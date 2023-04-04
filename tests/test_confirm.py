from pages.alert import Alert
import allure
import time


@allure.title('Отмена Алерта')
def test_confirm(browser):
    demo_page = Alert(browser)
    demo_page.visit()

    demo_page.btn_confirm.click()
    time.sleep(2)
    demo_page.alert().dismiss()

    assert demo_page.confirm_result.get_text() == 'You selected Cancel'

