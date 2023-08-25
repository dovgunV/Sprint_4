from selenium.webdriver.common.by import By


class OrderLocators:
    input_name = (By.XPATH, ".//input[@placeholder='* Имя']")
    input_last_name = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    input_address = (
        By.XPATH,
        ".//input[@placeholder='* Адрес: куда привезти заказ']",
    )
    input_metro = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    station = (By.XPATH, ".//div[contains(text(), '{station}')]/../..")
    input_telephone = (
        By.XPATH,
        ".//input[@placeholder='* Телефон: на него позвонит курьер']",
    )
    btn_next = (By.XPATH, ".//button [contains(text(), 'Далее')]")
    input_date = (
        By.XPATH,
        ".//input[@placeholder='* Когда привезти самокат']",
    )
    today = (By.CLASS_NAME, "react-datepicker__day--today")
    input_rental_period = (By.CLASS_NAME, "Dropdown-root")
    period = (
        By.XPATH,
        ".//div[@class='Dropdown-option' and text()= '{period}']",
    )
    btn_order = (
        By.XPATH,
        ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM'"
        "and text()='Заказать']",
    )
    confirmation_window = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    confirm = (By.XPATH, ".//button[text()= 'Да']")
    order_window = (By.CLASS_NAME, "Order_Text__2broi")
    black_color = (By.ID, "black")
