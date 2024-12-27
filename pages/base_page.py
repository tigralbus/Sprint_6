from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators.general_locators import GeneralLocators
from locators.order_page_locators import OrderPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = Constants.URL

    # кликнуть ссылку на яндекс
    def click_yandex(self):
        self.click_locator(GeneralLocators.YANDEX_LINK)

    # кликнуть ссылку на самокат
    def click_scooter(self):
        self.click_locator(GeneralLocators.SCOOTER_LINK)

    # кликнуть на верхнюю кнопку Заказать
    def click_order_button(self):
        self.click_locator(GeneralLocators.UPPER_ORDER_BUTTON)

    # кликнуть на верхнюю кнопку Статус
    def click_status_button(self):
        self.click_locator(OrderPageLocators.STATUS_BUTTON)

    def go_to_site(self):
        self.driver.get(self.url)

    # кликнуть на элемент
    def click_locator(self, locator):
        self.find_element(locator, 10).click()

    # проскроллить страницу вниз до конца
    def scroll_till_end(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # подождать пока появится локатор
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            expected_conditions.visibility_of_element_located(locator), message=f'Not find element {locator}')

    # подождать загрузку урла
    def await_url(self, url, time=10):
        return WebDriverWait(self.driver, time).until(
            expected_conditions.url_to_be(Constants.YA_DZEN_URL),
            message=f"URL did not match exactly: {url}")

    # получить текст элемента
    def get_element_text(self, locator):
        text = self.driver.find_element(*locator).text
        return text

    # заполнить текстовое поле
    def fill_field(self, field_name, field_value):
        element = self.driver.find_element(*field_name)
        element.send_keys(field_value)

    # выбрать день в календаре
    def fill_calendar_date(self, date_field, date_value):
        date = self.driver.find_element(*date_field)
        date.send_keys(date_value)
        date.send_keys(Keys.RETURN)  # Подтвердить

    # select checkbox by value
    def select_checkbox_by_value(self, value):
        checkbox = [By.ID, value]
        self.click_locator(checkbox)
