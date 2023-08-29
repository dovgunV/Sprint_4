from selenium.webdriver.common.by import By


class SellingLocators:
    logo_yandex = (By.XPATH, './/img[@alt="Yandex"]')
    logo_scooter = (By.XPATH, './/img[@alt="Scooter"]')
    btn_order_header = (
        By.XPATH,
        ".//div[@class='Header_Nav__AGCXC']"
        "/button[@class='Button_Button__ra12g']",
    )
    questions = (By.XPATH, './/div[contains(text(),"Вопросы о важном")]')
    question = (By.ID, "accordion__heading-{id}")
    answer = (By.ID, "accordion__panel-{id}")
    btn_order = (
        By.XPATH,
        ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']",
    )
