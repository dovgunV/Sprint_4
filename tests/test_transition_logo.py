from selenium.webdriver.firefox.webdriver import WebDriver

from pages.order_page import OrderPage
from pages.selling_page import SellingPage
from pages.yandex_page import YandexPage
from urls import BASE, YANDEX


class TestTransitionLogo:
    def test_transition_logo_yandex_from_general_page_new_page_yandex(
        self, driver: WebDriver
    ) -> None:
        SellingPage(driver).click_yandex_logo()
        driver.switch_to.window(driver.window_handles[1])
        YandexPage(driver).expect_availability()
        assert driver.current_url == YANDEX

    def test_transition_logo_yandex_from_order_page_new_page_yandex(
        self, driver: WebDriver
    ) -> None:
        SellingPage(driver).click_ordering_from_header()
        OrderPage(driver).click_yandex_logo()
        driver.switch_to.window(driver.window_handles[1])
        YandexPage(driver).expect_availability()
        assert driver.current_url == YANDEX

    def test_transition_logo_scooter_from_order_page_selling_page(
        self, driver: WebDriver
    ) -> None:
        SellingPage(driver).click_ordering_from_header()
        OrderPage(driver).click_scooter_logo()
        assert driver.current_url == BASE
