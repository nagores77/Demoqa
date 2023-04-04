from pages.alert import Alert
import allure
import time


@allure.title('Проверка видимости Alerts')
def test_web_tables(browser): #test#1
    demo_page = Alert(browser)
    demo_page.visit()

    assert not demo_page.alert()  # проверяем, что алерта нет
    demo_page.btn_alert.click()
    time.sleep(2)
    assert demo_page.alert() #проверяем, что алерт есть
    demo_page.alert().accept() #close alert window


def test_alert_text(browser): #test#2
    demo_page = Alert(browser)
    demo_page.visit()
    demo_page.btn_alert.click()
    time.sleep(2)

    assert demo_page.alert().text == 'You clicked a button' # check alert text content
    demo_page.alert().accept() #'confirm' alert window
    assert not demo_page.alert()


