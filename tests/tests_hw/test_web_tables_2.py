from pages.webtables import WebTables
import allure
import time
from selenium.webdriver.common.keys import Keys


@allure.severity(allure.severity_level.NORMAL)
@allure.feature('check attr')

def test_web_tables(browser):

    demo_page = WebTables(browser)
    demo_page.visit()

    demo_page.btn_rows.send_keys('5 rows')
    demo_page.btn_rows.send_keys(Keys.ENTER)


    demo_page.btn_next.click()
    assert demo_page.get_url() == 'https://demoqa.com/webtables'
    demo_page.btn_previous.click()
    assert demo_page.get_url() == 'https://demoqa.com/webtables'

    assert demo_page.btn_next.get_dom_attribute('disabled')
    assert demo_page.btn_previous.get_dom_attribute('disabled')

    demo_page.Add.click()  #plus1
    demo_page.first_name.send_keys(text='Helena')
    demo_page.last_name.send_keys(text='Kim')
    demo_page.user_email.send_keys(text='piman@gmail.com')
    demo_page.user_age.send_keys(text='28')
    demo_page.user_salary.send_keys(text='250')
    demo_page.user_department.send_keys(text='QA')
    demo_page.btn_submit.click_force()

    demo_page.Add.click()  # plus2
    demo_page.first_name.send_keys(text='Elena')
    demo_page.last_name.send_keys(text='Fox')
    demo_page.user_email.send_keys(text='ivan@gmail.com')
    demo_page.user_age.send_keys(text='30')
    demo_page.user_salary.send_keys(text='250')
    demo_page.user_department.send_keys(text='QA E')
    demo_page.btn_submit.click_force()

    demo_page.Add.click()  # plus3
    demo_page.first_name.send_keys(text='Joy')
    demo_page.last_name.send_keys(text='Wo')
    demo_page.user_email.send_keys(text='veg@gmail.com')
    demo_page.user_age.send_keys(text='25')
    demo_page.user_salary.send_keys(text='250')
    demo_page.user_department.send_keys(text='QA En')
    demo_page.btn_submit.click_force()
    time.sleep(10)

    assert demo_page.page_of.get_text() == '2'
    assert demo_page.btn_next.get_dom_attribute('class') == '-btn'

    demo_page.btn_next.click_force()
    time.sleep(3)
    demo_page.btn_previous.click_force()
    time.sleep(10)
    #assert demo_page.page_number.get_text() == '1' - не прошел







