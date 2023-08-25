from selenium.webdriver.common.by import By


class GeneralLocators:
    logo_yandex = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    logo_scooter = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    btn_order = (
        By.XPATH,
        ".//div[@class='Header_Nav__AGCXC']"
        "/button[@class='Button_Button__ra12g']",
    )
