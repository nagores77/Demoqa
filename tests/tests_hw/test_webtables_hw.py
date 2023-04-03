from pages.webtables import WebTables
import allure


@allure.severity(allure.severity_level.BLOCKER)
@allure.feature('check attr')
@allure.story('Проверка отсутствия атрибута')
def test_web_tables(browser):

    demo_page = WebTables(browser)
    demo_page.visit()

    demo_page.Add.click()
    assert demo_page.dialog_window.exist()

    demo_page.btn_submit.click_force()
    assert demo_page.form_validation.get_dom_attribute('class') == 'was-validated'

    demo_page.first_name.send_keys(text='Helena')
    demo_page.last_name.send_keys(text='Kim')
    demo_page.user_email.send_keys(text='piman@gmail.com')
    demo_page.user_age.send_keys(text='28')
    demo_page.user_salary.send_keys(text='250')
    demo_page.user_department.send_keys(text='QA')

    demo_page.btn_submit.click_force()
    assert not demo_page.dialog_window.exist()
    assert demo_page.user_record.exist()

    demo_page.pencil_edit.click()
    assert demo_page.dialog_window.exist()

    demo_page.first_name.clear()
    demo_page.first_name.send_keys(text='Elena')
    demo_page.btn_submit.click_force()
    assert demo_page.user_record.get_text() == 'Elena'

    demo_page.record_bin.click()
    assert not demo_page.user_record.get_text() == ''







