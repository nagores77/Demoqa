from pages.text_box import TextBox
import allure


@allure.feature('check attr')                      #проверка значения атрибута элемента
@allure.story('Проверка отсутствия атрибута')      #проверка отсутствия атрибута
@allure.severity(allure.severity_level.BLOCKER)    #важность тест-кейса; виды: BLOCKER, CRITICAL, NORMAL, MINOR
def test_placeholder(browser):

    demo_page = TextBox(browser)
    demo_page.visit()

    assert demo_page.first_line.get_dom_attribute('placeholder') == 'Full Name'
def test_fail():
    assert 111 == 222