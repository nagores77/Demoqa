from pages.webtables import WebTables
import allure
import time


@allure.title('Веб_элементы')
def test_web_tables(browser):
    demo_page = WebTables(browser)
    demo_page.visit()

#Проверяем, что нет незаполненных строк
    assert not demo_page.no_rows_found.exist()

# Удаляем записи:
    while demo_page.delete_rows.exist():
        demo_page.delete_rows.click()

    time.sleep(2)

    assert demo_page.no_rows_found.exist()


