import allure

from conftest import driver
from constants import Constants
from pages.main_page import MainPageScooter
from pages.order_page_rent import OrderPageRent
from pages.order_page_who import OrderPageWho


class TestPagesNavigation:
    @allure.title('Проверка перехода с главной страницы Самоката на Яндекс Дзен.')
    def test_redirect_to_ya_dzen_from_main_page(self, driver):
        page = self.open_home_page(driver)
        self.assert_redirect_to_yandex(page, driver)

    @allure.title('Проверка перехода со страницы ввода персональных данных заказа на Яндекс Дзен.')
    def test_redirect_to_ya_dzen_from_order_who_page(self, driver):
        page = self.open_who_page(driver)
        self.assert_redirect_to_yandex(page, driver)

    @allure.title('Проверка перехода со страницы ввода деталей заказа на Яндекс Дзен.')
    def test_redirect_to_ya_dzen_from_order_rent_page(self, driver):
        page = self.open_rent_page(driver)
        self.assert_redirect_to_yandex(page, driver)

    @allure.title('Проверка перехода с главной страницы по лого Самокат.')
    def test_redirect_to_main_page_on_main_page(self, driver):
        page = self.open_home_page(driver)
        self.assert_redirect_to_main(page, driver)

    @allure.title('Проверка перехода со страницы ввода персональных данных заказа по лого Самокат.')
    def test_redirect_to_main_page_from_order_who_page(self, driver):
        page = self.open_who_page(driver)
        self.assert_redirect_to_main(page, driver)

    @allure.title('Проверка перехода со страницы ввода деталей заказа по лого Самокат.')
    def test_redirect_to_main_page_from_order_rent_page(self, driver):
        page = self.open_rent_page(driver)
        self.assert_redirect_to_main(page, driver)

    def open_home_page(self, driver):
        home_page = MainPageScooter(driver)
        home_page.go_to_site()
        home_page.await_loaded()
        return home_page

    def open_who_page(self, driver):
        self.open_home_page(driver).click_order_button()
        page = OrderPageWho(driver)
        page.await_loaded()
        return page

    def open_rent_page(self, driver):
        page = self.open_who_page(driver)
        page.fill_personal_data('Имя', 'Фамилия', 'адрес', 'Курская', '89871234567')
        page.click_next()
        page = OrderPageRent(driver)
        page.await_loaded()
        return page

    @staticmethod
    def assert_redirect_to_yandex(page, driver):
        page.click_yandex()
        assert len(page.get_tabs_list()) == 2
        page.switch_to_tab(1)
        page.await_url(Constants.YA_DZEN_URL)

    @staticmethod
    def assert_redirect_to_main(page, driver):
        page.click_scooter()

        new_page = MainPageScooter(driver)
        new_page.await_loaded()

        assert len(new_page.get_tabs_list()) == 1
        assert new_page.get_current_url() == Constants.URL