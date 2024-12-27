import allure

from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class MainPageScooter(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('подождать загрузку главной страницы')
    def await_loaded(self):
        self.find_element(MainPageLocators.MAIN_PAGE_HEADER)

    @allure.step('кликнуть на нижнюю кнопку Заказать')
    def click_lower_order_button(self):
        button = self.find_element(OrderPageLocators.LOWER_ORDER_BUTTON)
        # при дефолтном скролле закрыто с подтверждением куки
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        button.click()

    @allure.step('раскрыть ответ на вопрос')
    def get_answer(self, question_locator, answer_locator):
        self.find_element(question_locator)
        self.click_locator(question_locator)
        self.find_element(answer_locator)
        return self.get_element_text(answer_locator)
