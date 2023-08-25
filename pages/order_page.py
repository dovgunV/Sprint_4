from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import TIMEOUT
from locators.general_locators import GeneralLocators
from locators.order_locators import OrderLocators
from pages.general_page import GeneralPage


class OrderPage(GeneralPage):
    def set_name(self, name: str) -> None:
        self._driver.find_element(*OrderLocators.input_name).send_keys(name)

    def set_last_name(self, last_name: str) -> None:
        self._driver.find_element(*OrderLocators.input_last_name).send_keys(
            last_name
        )

    def set_address(self, address: str) -> None:
        self._driver.find_element(*OrderLocators.input_address).send_keys(
            address
        )

    def set_metro(self, station: str) -> None:
        self._driver.find_element(*OrderLocators.input_metro).click()
        strategy, locator = OrderLocators.station
        self._driver.find_element(
            strategy, locator.format(station=station)
        ).click()

    def set_telephone(self, telephone: int) -> None:
        self._driver.find_element(*OrderLocators.input_telephone).send_keys(
            telephone
        )

    def next(self) -> None:
        self._driver.find_element(*OrderLocators.btn_next).click()

    def click_calendar(self) -> None:
        self._driver.find_element(*OrderLocators.input_date).click()

    def click_today(self) -> None:
        self._driver.find_element(*OrderLocators.today).click()

    def period_selection(self, period: str) -> None:
        self._driver.find_element(*OrderLocators.input_rental_period).click()
        strategy, locator = OrderLocators.period
        self._driver.find_element(
            strategy, locator.format(period=period)
        ).click()

    def order(self) -> None:
        self._driver.find_element(*OrderLocators.btn_order).click()

    def confirm_order(self) -> None:
        WebDriverWait(self._driver, TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                OrderLocators.confirmation_window
            )
        )
        self._driver.find_element(*OrderLocators.confirm).click()

    def order_text(self) -> str:
        WebDriverWait(self._driver, TIMEOUT).until(
            expected_conditions.visibility_of_element_located(
                OrderLocators.order_window
            )
        )
        return self._driver.find_element(*OrderLocators.order_window).text

    def choose_black_color(self) -> None:
        self._driver.find_element(*OrderLocators.black_color).click()

    def click_yandex_logo(self) -> None:
        self._driver.find_element(*GeneralLocators.logo_yandex).click()

    def click_scooter_logo(self) -> None:
        self._driver.find_element(*GeneralLocators.logo_scooter).click()
