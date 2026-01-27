from selenium.webdriver.common.by import By

class MainPageLocators:
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class,'Header_Nav')]//button[normalize-space(.)='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]//button[normalize-space(.)='Заказать']")

    FAQ_ITEMS = (By.CSS_SELECTOR, "div[data-accordion-component='AccordionItemButton']")

    YANDEX_LOGO_LINK = (By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI")
    SCOOTER_LOGO = (By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR")

    COOKIE_ACCEPT = (By.ID, "rcc-confirm-button")
