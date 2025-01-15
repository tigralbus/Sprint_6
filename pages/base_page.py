import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = Constants.URL

    def await_loaded(self):
        self.find_element(self.page_locator())

    def page_locator(self):
        return None

    @allure.step('кликнуть ссылку на яндекс')
    def click_yandex(self):
        self.click_locator(BasePageLocators.YANDEX_LINK)

    @allure.step('кликнуть ссылку на самокат')
    def click_scooter(self):
        self.click_locator(BasePageLocators.SCOOTER_LINK)

    @allure.step('кликнуть на верхнюю кнопку Заказать')
    def click_order_button(self):
        self.click_locator(BasePageLocators.UPPER_ORDER_BUTTON)

    @allure.step('перейти на стартовую страницу')
    def go_to_site(self):
        self.driver.get(self.url)

    @allure.step('кликнуть на элемент')
    def click_locator(self, locator):
        self.find_element(locator, 10).click()

    @allure.step('проскроллить страницу вниз до конца')
    def scroll_till_end(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step('проскроллить страницу к элементу')
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('подождать пока появится локатор')
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            expected_conditions.visibility_of_element_located(locator), message=f'Not find element {locator}')

    @allure.step('подождать загрузку урла {url}')
    def await_url(self, url, time=10):
        return WebDriverWait(self.driver, time).until(
            expected_conditions.url_to_be(Constants.YA_DZEN_URL),
            message=f"URL did not match exactly: {url}")

    @allure.step('получить текст элемента')
    def get_element_text(self, locator):
        text = self.driver.find_element(*locator).text
        return text

    @allure.step('заполнить текстовое поле')
    def fill_field(self, field_name, field_value):
        element = self.driver.find_element(*field_name)
        element.send_keys(field_value)

    @allure.step('выбрать день в календаре')
    def fill_calendar_date(self, date_field, date_value):
        date = self.driver.find_element(*date_field)
        date.send_keys(date_value)
        date.send_keys(Keys.RETURN)  # Подтвердить

    @allure.step('выбрать значение чекбокса')
    def select_checkbox_by_value(self, value):
        checkbox = [By.ID, value]
        self.click_locator(checkbox)

    @allure.step('получить список открытых табов')
    def get_tabs_list(self):
        return self.driver.window_handles

    @allure.step('переключиться на табу {tab_number}')
    def switch_to_tab(self, tab_number):
        self.driver.switch_to.window(self.get_tabs_list()[tab_number])

    @allure.step('получить урл текущей табы')
    def get_current_url(self):
        return self.driver.current_url
