import pytest
import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.rent_page import RentPage
from data.order_data import ORDER_DATASETS


@allure.feature("Order")
class TestOrderFlow:
    @pytest.mark.parametrize("entry_point", ["top", "bottom"])
    @pytest.mark.parametrize("data", ORDER_DATASETS)
    def test_create_order_success(self, driver, entry_point, data):
        main = MainPage(driver)
        main.open()
        main.accept_cookies_if_present()

        if entry_point == "top":
            main.click_order_top()
        else:
            main.click_order_bottom()

        step1 = OrderPage(driver)
        step1.wait_loaded()
        step1.fill_step1(
            first_name=data["first_name"],
            last_name=data["last_name"],
            address=data["address"],
            metro=data["metro"],
            phone=data["phone"],
        )
        step1.go_next()

        step2 = RentPage(driver)
        step2.wait_loaded()
        step2.pick_date_first_available()
        step2.pick_rent_period("сутки")
        step2.pick_color(black=True, grey=False)
        step2.add_comment(data["comment"])
        step2.submit_and_confirm()
        step2.success_modal_visible()
