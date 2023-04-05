from pages.text_box import TextBox
import allure
import time


def test_text_box_submit(browser):

    text_box = TextBox(browser)
    text_box.visit()

    assert text_box.btn_submit.check_css('color', '#fff')

    assert text_box.btn_submit.check_css('backgroundColor', '#007bff')
    assert text_box.btn_submit.check_css('borderColor', '#007bff')

# CamelCase (...без пробела, кажд послед - с заглавной буквы) - стиль нейминга
# snake_case_(...через нижн подчеркивание, послед = со строчной буквы)