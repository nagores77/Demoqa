from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from components.components import WebElement
from selenium.webdriver.common.by import By


class WebTables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)
        self.pageData = {'title': 'DEMOQA'}
        self.Add = WebElement(driver, '#addNewRecordButton')
        self.dialog_window = WebElement(driver, 'body > div.fade.modal.show > div > div > div.modal-body')
        self.btn_submit = WebElement(driver, '#submit')
        self.form_validation = WebElement(driver, '#userForm')
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.user_age = WebElement(driver, '#age')
        self.user_salary = WebElement(driver, '#salary')
        self.user_department = WebElement(driver, '#department')
        self.user_record = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(1)')
        self.pencil_edit = WebElement(driver, '#edit-record-4 > svg > path')
        self.record_bin = WebElement(driver, '#delete-record-4 > svg > path')

        self.btn_rows = WebElement(driver, '.select-wrap select')
        self.btn_next = WebElement(driver, '.-next > button:nth-child(1)')
        self.btn_previous = WebElement(driver, '.-previous > button:nth-child(1)')
        self.page_of = WebElement(driver, 'span.-pageInfo >span')
        #self.page_number = WebElement(driver, 'span.-pageInfo > div > input[type=number]')

        self.delete_rows = WebElement(driver, '[title="Delete"]')
        self.no_rows_found = WebElement(driver, 'div.rt-noData')

        self.webtable_header = WebElement(driver, 'div.rt-resizable-header-content')
        self.webtable_content = WebElement(driver, 'div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody')






0