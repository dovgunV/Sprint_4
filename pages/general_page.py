from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class GeneralPage:
    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver

    def _scroll_to_element(self, element: WebElement) -> None:
        element.location_once_scrolled_into_view
        ActionChains(self._driver).move_to_element(element).perform()
