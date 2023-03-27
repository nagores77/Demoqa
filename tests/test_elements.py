from pages.elements_page import ElementsPage


def test_find_elements(browser):
    demo_page = ElementsPage(browser)
    demo_page.visit()
    assert demo_page.btns_first_menu.check_count_elements(count=9)
