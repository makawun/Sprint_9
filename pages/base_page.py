from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.urls import Urls


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, path: str = ""):
        self._driver.get(f"{Urls.BASE}{path}")

    def get_current_url(self) -> str:
        return self._driver.current_url

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def click_when_visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator)).click()

    def click_js(self, locator):
        element = self.find(locator)
        self._driver.execute_script("arguments[0].click();", element)

    def fill(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def is_visible(self, locator) -> bool:
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    def upload_file(self, locator, file_path: str):
        self.find(locator).send_keys(file_path)

    def submit_form_js(self):
        form = self.find((By.TAG_NAME, "form"))
        self._driver.execute_script("arguments[0].requestSubmit();", form)