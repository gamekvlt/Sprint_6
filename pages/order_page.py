from __future__ import annotations

import allure
from selenium.webdriver.common.by import By

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step("Wait for order step 1 header")
    def wait_loaded(self) -> None:
        self.wait_visible(OrderPageLocators.HEADER)

    @allure.step("Fill step 1 form (who is the scooter for)")
    def fill_step1(self, first_name: str, last_name: str, address: str, metro: str, phone: str) -> None:
        self.type(OrderPageLocators.FIRST_NAME_INPUT, first_name)
        self.type(OrderPageLocators.LAST_NAME_INPUT, last_name)
        self.type(OrderPageLocators.ADDRESS_INPUT, address)

        self.click(OrderPageLocators.METRO_INPUT)
        option = (
            By.XPATH,
            f"//button[contains(@class,'select-search__option')][.//div[normalize-space(.)='{metro}']]",
        )
        self.click(option)

        self.type(OrderPageLocators.PHONE_INPUT, phone)

    @allure.step("Go to step 2")
    def go_next(self) -> None:
        self.click(OrderPageLocators.NEXT_BUTTON)
