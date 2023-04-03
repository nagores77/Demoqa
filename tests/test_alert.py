from pages.alert import Alert
import allure
import time


@allure.title('Проверка видимости Alerts')
def test_web_tables(browser):
    demo_page = Alert(browser)
    demo_page.visit()

    assert not demo_page.alert()  # проверяем, что алерта нет
    demo_page.btn_alert.click()
    time.sleep(2)

    assert demo_page.alert() #проверяем, что алерт есть

