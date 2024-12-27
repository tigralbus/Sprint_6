from selenium.webdriver.common.by import By

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPageWho(BasePage):

    def await_loaded(self):
        self.find_element(OrderPageLocators.PERSONAL_DATA_FORM_HEADER)

    def set_name(self, name):
        self.fill_field(OrderPageLocators.NAME_FIELD, name)

    def set_surname(self, surname):
        self.fill_field(OrderPageLocators.SURNAME_FIELD, surname)

    def set_address(self, address):
        self.fill_field(OrderPageLocators.ADDRESS_FIELD, address)

    def set_metro(self, metro_name):
        self.click_locator(OrderPageLocators.METRO_STATION_FIELD)
        self.click_locator(
            [By.XPATH, f"//div[@class='select-search__select']//button/div[contains(text(), '{metro_name}')]"])

    def set_phone(self, phone):
        self.fill_field(OrderPageLocators.PHONE_FIELD, phone)

    def click_next(self):
        self.click_locator(OrderPageLocators.NEXT_BUTTON)

    # заполнить поля 1 шага и не кликать Далее
    def fill_personal_data(self, name, surname, address, metro_name, phone):
        # заполнить поле имени
        self.set_name(name)
        # заполнить поле фамилии
        self.set_surname(surname)
        # заполнить поле адрес
        self.set_address(address)
        # выбрать метро из списка
        self.set_metro(metro_name)
        # заполнить поле телефон
        self.set_phone(phone)