from pages.text_box import TextBox
import time

def test_clear(browser):

    demo_page = TextBox(browser)
    demo_page.visit()

    demo_page.first_line.send_keys('Spring')
    time.sleep(2)
    demo_page.first_line.clear()
    time.sleep(2)

    assert demo_page.first_line.get_text() == ''


