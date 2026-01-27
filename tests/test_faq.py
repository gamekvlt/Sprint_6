import pytest
import allure

from pages.main_page import MainPage
from data.faq_data import FAQ_ITEMS


@allure.feature("FAQ")
class TestFAQ:
    @pytest.mark.parametrize("faq_index, expected_substring", FAQ_ITEMS)
    def test_faq_answer_opens(self, driver, faq_index, expected_substring):
        page = MainPage(driver)
        page.open()
        page.accept_cookies_if_present()

        answer_text = page.open_faq_item(faq_index)

        assert expected_substring in answer_text, f"Expected substring not found for FAQ index {faq_index}"
