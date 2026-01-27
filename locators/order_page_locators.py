from selenium.webdriver.common.by import By

class OrderPageLocators:
    HEADER = (By.XPATH, "//div[contains(@class,'Order_Header') and normalize-space(.)='Для кого самокат']")

    FIRST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.CSS_SELECTOR, "input.select-search__input")

    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[normalize-space(.)='Далее']")
