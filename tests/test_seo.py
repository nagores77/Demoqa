from pages.demoqa import DemoQa


def test_check_title_demo(browser):

    demo_page_1 = DemoQa(browser)
    demo_page_1.visit()
    assert browser.title == demo_page_1.pageData['title']