from pages.form_page import FormPage
import time


def test_login_form_validate(browser):

    demo_page = FormPage(browser)
    demo_page.visit()
    assert demo_page.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert demo_page.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert demo_page.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    assert demo_page.user_email.get_dom_attribute('pattern') == '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'

    demo_page.btn_submit.click_force()
    assert demo_page.form_validation.get_dom_attribute('class') == 'was-validated'
