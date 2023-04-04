from pages.modal_dialogs import ModalDialogs
import time
import pytest
import allure


@allure.title('Проверка модальных окон')
@pytest.mark.xfail(condition=True, reason='Если страница недоступна, тест будет помечен, как xfail')
def test_check_modal(browser):

    demo_page = ModalDialogs(browser)

    demo_page.visit()

    assert demo_page.small_modal.exist()
    assert demo_page.large_modal.exist()

    demo_page.small_modal.click()
    time.sleep(2)
    assert demo_page.small_modal_alert.exist()
    demo_page.btn_close_small_modal.click()
    time.sleep(2)
    demo_page.large_modal.click()
    time.sleep(2)
    assert demo_page.large_modal_alert.exist()
    time.sleep(2)
    demo_page.btn_close_large_modal.click()




