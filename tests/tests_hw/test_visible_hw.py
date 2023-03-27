from pages.accordion import Accordion
import time


def test_visible_accordion(browser):

    demo_page = Accordion(browser)
    demo_page.visit()

    assert demo_page.text_block.visible()
    demo_page.heading.click()

    time.sleep(2)

    assert not demo_page.text_block.visible()


def test_visible_accordion_default(browser):
    demo_page = Accordion(browser)
    demo_page.visit()

