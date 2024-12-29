import allure

from conftest import driver
from constants import Constants
from pages.main_page import MainPageScooter
from pages.order_page_rent import OrderPageRent
from pages.order_page_who import OrderPageWho


class TestPagesNavigation:
    @allure.title('Проверка перехода с главной страницы Самоката на Яндекс Дзен.')
    def test_redirect_to_ya_dzen_from_main_page(self, driver):
        home_page = MainPageScooter(driver)
        home_page.go_to_site()
        home_page.await_loaded()
        home_page.click_yandex()

        assert len(home_page.get_tabs_list()) == 2
        home_page.switch_to_tab(1)
        home_page.await_url(Constants.YA_DZEN_URL)

    @allure.title('Проверка перехода со страницы ввода персональных данных заказа на Яндекс Дзен.')
    def test_redirect_to_ya_dzen_from_order_who_page(self, driver):
        home_page = MainPageScooter(driver)
        home_page.go_to_site()
        home_page.await_loaded()
        home_page.click_scooter()
        home_page.click_order_button()

        page = OrderPageWho(driver)
        page.await_loaded()
        page.click_yandex()
        assert len(page.get_tabs_list()) == 2
        page.switch_to_tab(1)
        page.await_url(Constants.YA_DZEN_URL)

    @allure.title('Проверка перехода со страницы ввода деталей заказа на Яндекс Дзен.')
    def test_redirect_to_ya_dzen_from_order_rent_page(self, driver):
        home_page = MainPageScooter(driver)
        home_page.go_to_site()
        home_page.await_loaded()
        home_page.click_scooter()
        home_page.click_order_button()

        page = OrderPageWho(driver)
        page.await_loaded()
        page.fill_personal_data('Имя', 'Фамилия', 'адрес', 'Курская', '89871234567')
        page.click_next()
        page = OrderPageRent(driver)
        page.await_loaded()
        page.click_yandex()
        assert len(page.get_tabs_list()) == 2
        page.switch_to_tab(1)
        page.await_url(Constants.YA_DZEN_URL)

    @allure.title('Проверка перехода с главной страницы по лого Самокат.')
    def test_redirect_to_main_page_on_main_page(self, driver):
        home_page = MainPageScooter(driver)
        home_page.go_to_site()
        home_page.await_loaded()
        home_page.click_scooter()

        new_page = MainPageScooter(driver)
        new_page.await_loaded()

        assert len(new_page.get_tabs_list()) == 1
        assert new_page.get_current_url() == Constants.URL

    @allure.title('Проверка перехода со страницы ввода персональных данных заказа по лого Самокат.')
    def test_redirect_to_main_page_from_order_who_page(self, driver):
        home_page = MainPageScooter(driver)
        home_page.go_to_site()
        home_page.await_loaded()
        home_page.click_scooter()
        home_page.click_order_button()

        page = OrderPageWho(driver)
        page.await_loaded()
        page.click_scooter()

        new_page = MainPageScooter(driver)
        new_page.await_loaded()

        assert len(new_page.get_tabs_list()) == 1
        assert new_page.get_current_url() == Constants.URL

    @allure.title('Проверка перехода со страницы ввода деталей заказа по лого Самокат.')
    def test_redirect_to_main_page_from_order_rent_page(self, driver):
        home_page = MainPageScooter(driver)
        home_page.go_to_site()
        home_page.await_loaded()
        home_page.click_scooter()
        home_page.click_order_button()

        page = OrderPageWho(driver)
        page.await_loaded()
        page.fill_personal_data('Имя', 'Фамилия', 'адрес', 'Курская', '89871234567')
        page.click_next()
        page = OrderPageRent(driver)
        page.await_loaded()
        page.click_scooter()

        new_page = MainPageScooter(driver)
        new_page.await_loaded()

        assert len(new_page.get_tabs_list()) == 1
        assert new_page.get_current_url() == Constants.URL