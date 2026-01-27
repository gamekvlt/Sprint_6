import pytest
import allure

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--width=1280")
    options.add_argument("--height=900")

    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    driver.implicitly_wait(2)

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        drv = item.funcargs.get("driver")
        if drv:
            try:
                allure.attach(drv.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
                allure.attach(drv.page_source, name="page_source", attachment_type=allure.attachment_type.HTML)
            except Exception:
                pass
