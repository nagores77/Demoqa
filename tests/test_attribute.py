from pages.text_box import TextBox
import allure


@allure.feature('check attr')
def test_placeholder(browser):    #проверка значения атрибута элемента

    demo_page = TextBox(browser)
    demo_page.visit()

    assert demo_page.first_line.get_dom_attribute('placeholder') == 'Full Name'
