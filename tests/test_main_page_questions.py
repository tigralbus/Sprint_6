import allure
import pytest

from conftest import driver
from constants import Answers
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPageScooter


class TestMainPageQuestions:

    @pytest.mark.parametrize('question_locator, answer_locator, answer_text', [
        [MainPageLocators.COST_QUESTION, MainPageLocators.COST_QUESTION_ANSWER, Answers.cost_question_answer_text],
        [MainPageLocators.SEVERAL_SCOOTERS_QUESTION, MainPageLocators.SEVERAL_SCOOTERS_QUESTION_ANSWER,
         Answers.several_scooters_question_answer_text],
        [MainPageLocators.RENT_TIME_QUESTION, MainPageLocators.RENT_TIME_QUESTION_ANSWER,
         Answers.rent_time_question_answer_text],
        [MainPageLocators.ORDER_TODAY_QUESTION, MainPageLocators.ORDER_TODAY_QUESTION_ANSWER,
         Answers.order_today_question_answer_text],
        [MainPageLocators.CHANGE_RENT_TIME_QUESTION, MainPageLocators.CHANGE_RENT_TIME_QUESTION_ANSWER,
         Answers.change_rent_time_question_answer_text],
        [MainPageLocators.CHARGE_SCOOTER_QUESTION, MainPageLocators.CHARGE_SCOOTER_QUESTION_ANSWER,
         Answers.charge_scooter_question_answer_text],
        [MainPageLocators.DECLINE_ORDER_QUESTION, MainPageLocators.DECLINE_ORDER_QUESTION_ANSWER,
         Answers.decline_order_question_answer_text]])
    @allure.title('Главная страница: Проверка ответа на вопрос(7 вопросов).')
    def test_question_text_verification(self, driver, question_locator, answer_locator, answer_text):
        main_page = MainPageScooter(driver)
        main_page.go_to_site()
        main_page.scroll_till_end()
        assert answer_text == main_page.get_answer(
            question_locator,
            answer_locator), f"Ошибка: ожидается текст '{answer_text}', но получили '{main_page.get_answer(
            question_locator, answer_locator)}'"
