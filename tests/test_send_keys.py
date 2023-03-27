from pages.form_page import FormPage
import time


def test_send_keys(browser):

    demo_page = FormPage(browser)
    demo_page.visit()

    demo_page.first_name.send_keys('Lena')
    time.sleep(3)
    demo_page.last_name.send_keys('Nagores')
    time.sleep(3)
    demo_page.gender.send_keys('Female')
    time.sleep(3)
    demo_page.mobile.send_keys('+79119695204')
    time.sleep(3)