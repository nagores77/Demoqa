
from pages.demoqa import DemoQa


def test_icon_exist(browser):

    demo_page = DemoQa(browser)
    demo_page.visit()
    demo_page.icon.click()
    assert demo_page.equal_url()
    assert demo_page.icon.exist()



