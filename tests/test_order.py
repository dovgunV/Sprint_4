from selenium.webdriver.firefox.webdriver import WebDriver

from pages.order_page import OrderPage
from pages.selling_page import SellingPage
from utilities import Generator


class TestTransitionLogo:
    def test_ordering_from_button_header_order_processed(
        self, driver: WebDriver
    ) -> None:
        SellingPage(driver).click_ordering_from_header()
        page: OrderPage = OrderPage(driver)
        page.fill_info(
            Generator.string(),
            Generator.string(),
            Generator.string(5),
            "Сокольники",
            Generator.number(),
            "сутки",
        )
        page.order()
        page.confirm_order()
        assert "Номер заказа" in page.order_text()

    def test_ordering_from_button_order_processed(
        self, driver: WebDriver
    ) -> None:
        SellingPage(driver).click_ordering()
        page: OrderPage = OrderPage(driver)
        page.fill_info(
            Generator.string(),
            Generator.string(),
            Generator.string(5),
            "Черкизовская",
            Generator.number(),
            "двое суток",
            True,
        )
        page.order()
        page.confirm_order()
        assert "Номер заказа" in page.order_text()
