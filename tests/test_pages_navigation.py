import allure
import pytest

from conftest import driver
from constants import Constants
from pages.main_page import MainPageScooter
from pages.order_page_rent import OrderPageRent
from pages.order_page_who import OrderPageWho


class TestPagesNavigation:
    # переход по ссылке Дзена на разных этапах заказа
    @pytest.mark.parametrize('depth', [0, 1, 2])
    @allure.title('Проверка перехода со страниц Самоката на Яндекс Дзен.')
    def test_redirect_to_ya_dzen(self, driver, depth):
        home_page = MainPageScooter(driver)
        home_page.go_to_site()
        home_page.await_loaded()
        # на форме заполнения персональных данных
        if depth > 0:
            home_page.click_order_button()
            page = OrderPageWho(driver)
            page.await_loaded()
            # на форме заполнения деталей заказа
            if depth > 1:
                page.fill_personal_data('Имя', 'Фамилия', 'адрес', 'Курская', '89871234567')
                page.click_next()
                last_page = OrderPageRent(driver)
                last_page.await_loaded()

        home_page.click_yandex()

        assert len(driver.window_handles) == 2
        driver.switch_to.window(driver.window_handles[1])
        home_page.await_url(Constants.YA_DZEN_URL)

    # переход по лого Самоката на разных этапах заказа
    @pytest.mark.parametrize('depth', [0, 1, 2])
    @allure.title('Проверка перехода со страниц самоката на главную страницу')
    def test_redirect_to_main_page(self, driver, depth):
        home_page = MainPageScooter(driver)
        home_page.go_to_site()
        home_page.await_loaded()
        # на форме заполнения персональных данных
        if depth > 0:
            home_page.click_order_button()
            page = OrderPageWho(driver)
            page.await_loaded()
            # на форме заполнения деталей заказа
            if depth > 1:
                page.fill_personal_data('Имя', 'Фамилия', 'адрес', 'Курская', '89871234567')
                page.click_next()
                last_page = OrderPageRent(driver)
                last_page.await_loaded()

        home_page.click_scooter()

        new_page = MainPageScooter(driver)
        new_page.await_loaded()
        assert len(driver.window_handles) == 1
        assert driver.current_url == Constants.URL
