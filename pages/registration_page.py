from pages.base_page import BasePage
from locators.registration_page_locators import RegistrationPageLocators


class RegistrationPage(BasePage):
    def fill_form(self, user: dict):
        self.fill(RegistrationPageLocators.NAME_INPUT, user["first_name"])
        self.fill(RegistrationPageLocators.SURNAME_INPUT, user["last_name"])
        self.fill(RegistrationPageLocators.USERNAME_INPUT, user["username"])
        self.fill(RegistrationPageLocators.EMAIL_INPUT, user["email"])
        self.fill(RegistrationPageLocators.PASSWORD_INPUT, user["password"])

    def submit(self):
        self.submit_form_js()
        self.wait.until(lambda d: "/signup" not in d.current_url)