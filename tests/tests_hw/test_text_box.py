from pages.text_box import TextBox
import time


def test_text_box(browser):

    demo_page = TextBox(browser)
    demo_page.visit()

    demo_page.first_line.send_keys('Albert Einstein')
    demo_page.address_line.send_keys('New Jersey, USA')
    time.sleep(2)
    demo_page.btn_submit.click_force()
    assert demo_page.bottom_text.get_text() == 'Name:Albert Einstein\nCurrent Address :New Jersey, USA'


