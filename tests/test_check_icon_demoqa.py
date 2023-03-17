
from pages.demoqa import DemoQa


def test_icon_exist(browser):

    demo_page = DemoQa(browser)
    demo_page.visit()
    demo_page.click_on_the_icon()
    # assert demo_page.equal_url()
    assert demo_page.test_icon_exist()

