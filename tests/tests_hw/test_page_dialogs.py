from pages.modal_dialogs import ModalDialogs


def test_modal_elements(browser):

    demo_page = ModalDialogs(browser)
    demo_page.visit()
    assert demo_page.element_group.check_count_elements(count=6)
