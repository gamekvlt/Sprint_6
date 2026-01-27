from __future__ import annotations

import allure
from selenium.webdriver.common.by import By

from locators.rent_page_locators import RentPageLocators
from pages.base_page import BasePage


class RentPage(BasePage):
    @allure.step("Wait for order step 2 header")
    def wait_loaded(self) -> None:
        self.wait_visible(RentPageLocators.HEADER)

    @allure.step("Pick a delivery date")
    def pick_date_first_available(self) -> None:
        self.click(RentPageLocators.DATE_INPUT)
        self.click(RentPageLocators.DATE_PICKER_TOMORROW)

    @allure.step("Pick rent period: {period_text}")
    def pick_rent_period(self, period_text: str = "сутки") -> None:
        self.click(RentPageLocators.RENT_PERIOD_DROPDOWN)
        self.wait_visible(RentPageLocators.RENT_MENU)
        option = (
            By.XPATH,
            f"//div[contains(@class,'Dropdown-option') and normalize-space(.)='{period_text}']",
        )
        self.click(option)

    @allure.step("Pick color: black={black}, grey={grey}")
    def pick_color(self, black: bool = True, grey: bool = False) -> None:
        if black:
            self.click(RentPageLocators.COLOR_BLACK)
        if grey:
            self.click(RentPageLocators.COLOR_GREY)

    @allure.step("Add courier comment")
    def add_comment(self, comment: str) -> None:
        if comment:
            self.type(RentPageLocators.COMMENT_INPUT, comment)

    @allure.step("Submit order and confirm")
    def submit_and_confirm(self) -> None:
        self.click(RentPageLocators.ORDER_BUTTON)
        self.wait_visible(RentPageLocators.CONFIRM_MODAL_HEADER)
        self.click(RentPageLocators.CONFIRM_YES)
        self.wait_present(RentPageLocators.SUCCESS_MODAL_TEXT, timeout=60)

    @allure.step("Verify success modal is shown")
    def success_modal_visible(self) -> None:
        self.wait_present(RentPageLocators.SUCCESS_MODAL_TEXT, timeout=60)

    @allure.step("Click Scooter logo from order flow")
    def click_scooter_logo(self, locator) -> None:
        self.click(locator)
