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
        page.set_name(Generator.string())
        page.set_last_name(Generator.string())
        page.set_address(Generator.string(5))
        page.set_metro("Сокольники")
        page.set_telephone(Generator.number())
        page.next()
        page.click_calendar()
        page.click_today()
        page.period_selection("сутки")
        page.order()
        page.confirm_order()
        assert "Номер заказа" in page.order_text()

    def test_ordering_from_button_order_processed(
        self, driver: WebDriver
    ) -> None:
        SellingPage(driver).click_ordering()
        page: OrderPage = OrderPage(driver)
        page.set_name(Generator.string())
        page.set_last_name(Generator.string())
        page.set_address(Generator.string(5))
        page.set_metro("Черкизовская")
        page.set_telephone(Generator.number())
        page.next()
        page.click_calendar()
        page.click_today()
        page.period_selection("двое суток")
        page.choose_black_color()
        page.order()
        page.confirm_order()
        assert "Номер заказа" in page.order_text()
