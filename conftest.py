from typing import Iterator

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver

from urls import BASE


@pytest.fixture
def driver() -> Iterator[WebDriver]:
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    browser = webdriver.Firefox(options)
    browser.get(BASE)
    yield browser
    browser.quit()
