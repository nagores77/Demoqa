from pages.form_page import FormPage
import time
from selenium.webdriver.common.keys import Keys


def test_login_form(browser):

    demo_page = FormPage(browser)
    demo_page.visit()

    assert not demo_page.modal_dialog.exist()
    time.sleep(2)

    demo_page.first_name.send_keys('Lena')
    demo_page.last_name.send_keys('Nagores')
    demo_page.user_email.send_keys('nagores@yandex.ru')
    demo_page.gender_radio_2.click_force()
    demo_page.user_number.send_keys('7911969520')
    time.sleep(2)
    demo_page.btn_state_menu.scroll_to_element()
    time.sleep(3)
    demo_page.state_list.send_keys(text='Haryana')
    demo_page.state_list.send_keys(Keys.ENTER)
    time.sleep(2)
    demo_page.btn_city_menu.scroll_to_element()
    time.sleep(3)
    demo_page.city_list.send_keys(text='Panipat')
    demo_page.city_list.send_keys(Keys.ENTER)

    demo_page.btn_submit.click_force()
    time.sleep(2)
    assert demo_page.modal_dialog.exist()
    time.sleep(2)
    demo_page.btn_close_modal.click_force()
    time.sleep(2)















