from __future__ import annotations

from typing import Optional
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        self.driver = driver
        self.timeout = timeout

    def wait_visible(self, locator, timeout: Optional[int] = None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(EC.visibility_of_element_located(locator))

    def wait_present(self, locator, timeout: Optional[int] = None):
        """Wait until element is present in the DOM (visibility not required)."""
        return WebDriverWait(self.driver, timeout or self.timeout).until(EC.presence_of_element_located(locator))

    def wait_invisible(self, locator, timeout: Optional[int] = None) -> bool:
        """Wait until element becomes invisible or is removed from the DOM."""
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_clickable(self, locator, timeout: Optional[int] = None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(EC.element_to_be_clickable(locator))

    def click(self, locator, timeout: Optional[int] = None) -> None:
        el = self.wait_clickable(locator, timeout)
        el.click()

    def type(self, locator, text: str, timeout: Optional[int] = None) -> None:
        el = self.wait_visible(locator, timeout)
        el.clear()
        el.send_keys(text)

    def scroll_into_view(self, locator) -> None:
        el = self.wait_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)

    def get_url(self) -> str:
        return self.driver.current_url

    def wait_url_contains(self, part: str, timeout: Optional[int] = None) -> bool:
        """Wait until current URL contains a substring."""
        return WebDriverWait(self.driver, timeout or self.timeout).until(EC.url_contains(part))

    def get_window_handles(self) -> list:
        return self.driver.window_handles

    def switch_to_window(self, handle: str) -> None:
        self.driver.switch_to.window(handle)

    def close_current_window(self) -> None:
        self.driver.close()

    def switch_to_window(self, handle: str) -> None:
        self.driver.switch_to.window(handle)

    def close_current_window(self) -> None:
        self.driver.close()

    def switch_to_new_window(self, previous_handles: list[str]) -> None:
        """Switch to a newly opened browser window/tab."""
        WebDriverWait(self.driver, self.timeout).until(lambda d: len(d.window_handles) > len(previous_handles))
        new_handle = next(h for h in self.driver.window_handles if h not in previous_handles)
        self.driver.switch_to.window(new_handle)

    def safe_click(self, locator) -> None:
        """Scroll + click (useful for elements below the fold)."""
        self.scroll_into_view(locator)
        self.click(locator)

    def element_exists(self, locator, timeout: int = 2) -> bool:
        try:
            self.wait_visible(locator, timeout)
            return True
        except TimeoutException:
            return False
