from selenium.webdriver.common.by import By

class RentPageLocators:
    HEADER = (By.XPATH, "//div[contains(@class,'Order_Header') and normalize-space(.)='Про аренду']")

    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")

    DATE_PICKER_TOMORROW = (
        By.XPATH,
        "(//div[contains(@class,'react-datepicker__day--today') and @aria-disabled='false']"
        "/following::div[contains(@class,'react-datepicker__day') and @role='button'"
        " and @aria-disabled='false' and not(contains(@class,'react-datepicker__day--outside-month'))][1])",
    )

    RENT_PERIOD_DROPDOWN = (By.XPATH, "//div[contains(@class,'Dropdown-control')][.//div[normalize-space(.)='* Срок аренды']]")
    RENT_MENU = (By.CSS_SELECTOR, "div.Dropdown-menu")

    COLOR_BLACK = (By.CSS_SELECTOR, "input#black")
    COLOR_GREY = (By.CSS_SELECTOR, "input#grey")

    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Buttons')]//button[normalize-space(.)='Заказать']")

    CONFIRM_MODAL_HEADER = (
        By.XPATH,
        "//div[@class='Order_ModalHeader__3FDaJ' and contains(.,'Хотите оформить заказ')]",
    )
    CONFIRM_YES = (
        By.XPATH,
        "//div[@class='Order_ModalHeader__3FDaJ' and contains(.,'Хотите оформить заказ')]/following::button[normalize-space(.)='Да'][1]",
    )
    CONFIRM_NO = (
        By.XPATH,
        "//div[@class='Order_ModalHeader__3FDaJ' and contains(.,'Хотите оформить заказ')]/following::button[normalize-space(.)='Нет'][1]",
    )

    SUCCESS_MODAL_TEXT = (
        By.XPATH,
        "//div[@class='Order_ModalHeader__3FDaJ' and contains(.,'Заказ оформлен')]",
    )
