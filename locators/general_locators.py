from selenium.webdriver.common.by import By


class GeneralLocators:
    YANDEX_LINK = [By.XPATH, "//div[@class='Header_Logo__23yGT']/a[@class='Header_LogoYandex__3TSOI']"]
    SCOOTER_LINK = [By.XPATH, "//div[@class='Header_Logo__23yGT']/a[@class='Header_LogoScooter__3lsAR']"]
    UPPER_ORDER_BUTTON = [By.XPATH, "//div[@class='Header_Nav__AGCXC']/button[text() = 'Заказать']"]