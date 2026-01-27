import allure

from pages.main_page import MainPage
from data.urls import BASE_URL, DZEN_DOMAIN


@allure.feature("Logos")
class TestLogos:
    def test_scooter_logo_returns_to_main(self, driver):
        page = MainPage(driver)
        page.open()
        page.accept_cookies_if_present()

        page.click_order_top()
        page.click_scooter_logo()

        assert page.get_url().rstrip("/") == BASE_URL.rstrip("/")

    def test_yandex_logo_opens_dzen_in_new_window(self, driver):
        page = MainPage(driver)
        page.open()
        page.accept_cookies_if_present()

        handles_before = page.get_window_handles()[:]
        page.click_yandex_logo()
        page.switch_to_new_window(handles_before)

        page.wait_url_contains(DZEN_DOMAIN, timeout=10)
        assert DZEN_DOMAIN in page.get_url()

        page.close_current_window()
        page.switch_to_window(handles_before[0])
