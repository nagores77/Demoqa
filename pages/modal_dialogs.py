from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from components.components import WebElement


class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)
        self.pageData = {'title': 'DEMOQA'}
        self.element_group = WebElement(driver, '.show > ul > li')
        self.main_icon = WebElement(driver, '#app > header > a > img')
        self.small_modal = WebElement(driver, '#showSmallModal')
        self.large_modal = WebElement(driver, '#showLargeModal')
        self.small_modal_alert = WebElement(driver, 'body > div.fade.modal.show > div')
        self.large_modal_alert = WebElement(driver, 'body > div.fade.modal.show > div')
        self.btn_close_small_modal = WebElement(driver, '#closeSmallModal')
        self.btn_close_large_modal = WebElement(driver, '#closeLargeModal')


