from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import TIMEOUT
from locators.selling_locators import SellingLocators
from pages.general_page import GeneralPage


class SellingPage(GeneralPage):
    def scroll_to_questions(self) -> None:
        self._scroll_to_element(
            self._driver.find_element(*SellingLocators.questions)
        )

    def expand_answer(self, id: int) -> str:
        strategy, locator = SellingLocators.question
        self._driver.find_element(strategy, locator.format(id=id)).click()
        strategy, locator = SellingLocators.answer
        return (
            WebDriverWait(self._driver, TIMEOUT)
            .until(
                expected_conditions.visibility_of_element_located(
                    (strategy, locator.format(id=id))
                )
            )
            .text
        )

    def click_yandex_logo(self) -> None:
        self._driver.find_element(*SellingLocators.logo_yandex).click()

    def click_ordering_from_header(self) -> None:
        self._driver.find_element(*SellingLocators.btn_order_header).click()

    def click_ordering(self) -> None:
        self._scroll_to_element(
            self._driver.find_element(*SellingLocators.btn_order)
        )
        self._driver.find_element(*SellingLocators.btn_order).click()
