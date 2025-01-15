import pytest
from selenium import webdriver


@pytest.fixture  # фикстура, которая инициализирует драйвер
def driver(request):
    browser = webdriver.Firefox()
    yield browser
    browser.quit()
