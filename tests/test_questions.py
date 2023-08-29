import pytest
from selenium.webdriver.firefox.webdriver import WebDriver

from data import ANSWERS
from pages.selling_page import SellingPage


class TestQuestions:
    @pytest.mark.parametrize("id, answer", ANSWERS)
    def test_response_disclosure_answer_correct(
        self, driver: WebDriver, id: int, answer: str
    ) -> None:
        page: SellingPage = SellingPage(driver)
        page.scroll_to_questions()
        assert page.expand_answer(id) == answer
