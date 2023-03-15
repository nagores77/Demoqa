import pytest
from selenium import webdriver


@pytest.fixture(scope="session")  #декоратор: влияет на поведение функции
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

