from pages.form_page import FormPage
import time


def test_send_keys(browser):

    demo_page = FormPage(browser)
    demo_page.visit()

    demo_page.first_name.send_keys('Lena')
    time.sleep(3)