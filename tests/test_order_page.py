import allure
import pytest

from conftest import driver
from pages.main_page import MainPageScooter
from pages.order_page_rent import OrderPageRent
from pages.order_page_who import OrderPageWho


class TestOrderPage:
    @pytest.mark.parametrize(
        'use_top_button, name, surname, address, metro_name, phone, date, term, scooter_color, comment', [
            [True, 'Леонид', 'Леонидов', 'улица Пушкина, дом Колотушкина 666', 'Сокольники', '89119111234',
             '31.12.2024', 'сутки', 'black', 'Побыстрее'],
            [False, 'Филлип', 'Филлипов', 'там за туманами, вечными пьяными 4', 'Курская', '89991234567',
             '11.08.1986', 'шестеро суток', 'grey', 'Помедленнее']])
    @allure.title('Страница заказа: Проверка еnd-2-end сценария заказа самоката.')
    def test_order_scooter_case(self, driver, use_top_button, name, surname, address, metro_name, phone, date, term,
                                scooter_color,
                                comment):
        page = MainPageScooter(driver)
        page.go_to_site()
        page.await_loaded()

        if use_top_button:
            page.click_order_button()
        else:
            page.click_lower_order_button()

        page = OrderPageWho(driver)
        page.await_loaded()

        # заполнить персональные данные и кликнуть далее
        page.fill_personal_data(name, surname, address, metro_name, phone)
        page.click_next()

        # заполнить детали заказа
        page = OrderPageRent(driver)
        page.await_loaded()
        page.fill_rent_data(date, term, scooter_color, comment)

        # кликнуть Заказать
        page.click_order()
        page.await_confirmation_modal()
        page.submit_confirmation()

        completed_message = page.get_completed_header()
        assert completed_message.startswith("Заказ оформлен\nНомер заказа: ")
        assert completed_message.endswith(".  Запишите его:\nпригодится, чтобы отслеживать статус")
