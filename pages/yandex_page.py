from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import TIMEOUT
from locators.yandex_locators import YandexLocators
from pages.general_page import GeneralPage


class YandexPage(GeneralPage):
    def expect_availability(self) -> None:
        WebDriverWait(self._driver, TIMEOUT).until(
            expected_conditions.presence_of_element_located(
                YandexLocators.btn_login
            )
        )
