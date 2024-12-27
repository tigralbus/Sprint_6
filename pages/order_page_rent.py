import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPageRent(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def page_locator(self):
        return OrderPageLocators.RENT_DATA_FORM_HEADER

    @allure.step('выбрать дату доставки')
    def set_delivery_date(self, date):
        self.click_locator(OrderPageLocators.DELIVERY_DATE_FIELD)
        self.fill_calendar_date(OrderPageLocators.DELIVERY_DATE_FIELD, date)

    @allure.step('выбрать срок аренды')
    def set_rent_term(self, term):
        self.click_locator(OrderPageLocators.RENT_TERM_FIELD)
        self.click_locator(OrderPageLocators.rent_term_locator(term))

    @allure.step('выбрать цвет самоката')
    def set_color(self, scooter_color):
        self.select_checkbox_by_value(scooter_color)

    @allure.step('заполнить поле Комментарий')
    def set_comment(self, comment):
        self.fill_field(OrderPageLocators.COMMENT_FIELD, comment)

    @allure.step('нажать кнопку Назад')
    def click_back(self):
        self.click_locator(OrderPageLocators.BACK_BUTTON)

    @allure.step('нажать кнопку Заказать')
    def click_order(self):
        self.click_locator(OrderPageLocators.ORDER_BUTTON)

    @allure.step('дождаться окна подтверждения заказа')
    def await_confirmation_modal(self):
        self.find_element(OrderPageLocators.DO_YOU_WANT_ORDER_FORM_HEADER)

    @allure.step('нажать кнопку Да в окне подтверждения заказа')
    def submit_confirmation(self):
        self.click_locator(OrderPageLocators.YES_BUTTON)

    @allure.step('получить текст сообщения о создании заказа')
    def get_completed_header(self):
        return self.get_element_text(OrderPageLocators.ORDER_COMPLETED_FORM_HEADER)

    @allure.step('заполнить поля 2 шага и не кликать Заказать')
    def fill_rent_data(self, date, term, scooter_color, comment):
        # открыть календарь
        self.set_delivery_date(date)
        # выбрать срок аренды: 'шестеро суток'/'сутки'
        self.set_rent_term(term)
        # выбрать цвет из списка black / grey
        self.set_color(scooter_color)
        # ввести комментарий
        self.fill_field(OrderPageLocators.COMMENT_FIELD, comment)
