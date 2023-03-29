from pages.text_box import TextBox


def test_placeholder(browser):

    demo_page = TextBox(browser)
    demo_page.visit()

    assert demo_page.first_line.get_dom_attribute('placeholder') == 'Full Name'
