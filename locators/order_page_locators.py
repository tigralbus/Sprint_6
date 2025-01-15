from selenium.webdriver.common.by import By


class OrderPageLocators:
    PERSONAL_DATA_FORM_HEADER = [By.XPATH, ".//div[@class = 'Order_Header__BZXOb'][text() = 'Для кого самокат']"]
    NEXT_BUTTON = [By.CLASS_NAME, 'Button_Middle__1CSJM']

    NAME_FIELD = [By.XPATH, ".//input[@placeholder='* Имя']"]
    SURNAME_FIELD = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    ADDRESS_FIELD = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
    METRO_STATION_FIELD = [By.XPATH, ".//input[@placeholder='* Станция метро']"]
    METRO_NAME_SET1 = [By.XPATH, ".//button[@class='Order_SelectOption__82bhS select-search__option'][@value='50']"]
    METRO_NAME_SET2 = [By.XPATH, ".//button[@class='Order_SelectOption__82bhS select-search__option'][@value='10']"]
    PHONE_FIELD = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]

    BACK_BUTTON = [By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Назад']"]
    ORDER_BUTTON = [By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']"]
    RENT_DATA_FORM_HEADER = [By.XPATH, ".//div[@class = 'Order_Header__BZXOb'][text() = 'Про аренду']"]

    DELIVERY_DATE_FIELD = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]
    RENT_TERM_FIELD = [By.XPATH, ".//div[@class = 'Dropdown-placeholder'][text()='* Срок аренды']"]
    COMMENT_FIELD = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"]

    DO_YOU_WANT_ORDER_FORM_HEADER = [By.XPATH,
                                     ".//div[@class = 'Order_ModalHeader__3FDaJ'][text()='Хотите оформить заказ?']"]
    ORDER_COMPLETED_FORM_HEADER = [By.XPATH,
                                   ".//div[@class = 'Order_ModalHeader__3FDaJ'][contains(text(), 'Заказ оформлен')]"]
    ORDER_COMPLETED_FORM_MESSAGE = [By.XPATH,
                                    ".//div[@class = 'Order_ModalHeader__3FDaJ']/div[@class='Order_Text__2broi']"]
    YES_BUTTON = [By.XPATH, ".//button[text()='Да']"]

    @staticmethod
    def metro_station_locator(metro_name):
        return [By.XPATH, f"//div[@class='select-search__select']//button/div[contains(text(), '{metro_name}')]"]

    @staticmethod
    def rent_term_locator(term):
        return [By.XPATH, f"//div[@class='Dropdown-menu']//div[contains(text(), '{term}')]"]
