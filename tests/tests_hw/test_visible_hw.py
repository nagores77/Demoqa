from pages.accordion import Accordion


def test_visible_accordion(browser):

    demo_page = Accordion(browser)
    demo_page.visit()
