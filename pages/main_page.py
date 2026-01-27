from __future__ import annotations

import allure
from selenium.webdriver.common.by import By

from data.urls import BASE_URL
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Open main page")
    def open(self) -> None:
        self.driver.get(BASE_URL)

    @allure.step("Accept cookies if banner present")
    def accept_cookies_if_present(self) -> None:
        if self.element_exists(MainPageLocators.COOKIE_ACCEPT, timeout=2):
            self.click(MainPageLocators.COOKIE_ACCEPT)

    @allure.step("Click top order button")
    def click_order_top(self) -> None:
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Click bottom order button")
    def click_order_bottom(self) -> None:
        self.safe_click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Open FAQ item by index: {index}")
    def open_faq_item(self, index: int) -> str:
        """Open FAQ item by its position in the FAQ list and return answer text."""
        items = self.driver.find_elements(*MainPageLocators.FAQ_ITEMS)
        if index < 0 or index >= len(items):
            raise IndexError(f"FAQ index {index} out of range (found {len(items)} items)")

        heading_el = items[index]
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", heading_el)
        self.driver.execute_script("arguments[0].click();", heading_el)

        panel_id = heading_el.get_attribute("aria-controls")
        answer_locator = (By.ID, panel_id)
        answer_el = self.wait_visible(answer_locator)
        return answer_el.text

    @allure.step("Click Scooter logo")
    def click_scooter_logo(self) -> None:
        self.click(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Click Yandex logo (opens new tab/window)")
    def click_yandex_logo(self) -> None:
        self.click(MainPageLocators.YANDEX_LOGO_LINK)
