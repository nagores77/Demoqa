from pages.alert import Alert
import allure
import time


@allure.title('Отмена Алерта')
def test_confirm(browser):
    demo_page = Alert(browser)
    demo_page.visit()
    demo_page.btn_prompt.click()
    time.sleep(2)
    demo_page.alert().send_keys('Jack')
    demo_page.alert().accept()
    assert demo_page.prompt_result.get_text() == 'You entered Jack'
    time.sleep(2)

