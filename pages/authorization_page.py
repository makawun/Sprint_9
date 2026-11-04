from pages.base_page import BasePage
from locators.authorization_page_locators import AuthorizationPageLocators
from data.urls import Urls


class AuthorizationPage(BasePage):
    def open(self):
        super().open(Urls.LOGIN)

    def click_create_account(self):
        self.click(AuthorizationPageLocators.CREATE_ACCOUNT_BUTTON)

    def login(self, username, password):
        self.fill(AuthorizationPageLocators.EMAIL_INPUT, username)
        self.fill(AuthorizationPageLocators.PASSWORD_INPUT, password)
        self.click(AuthorizationPageLocators.LOG_IN_BUTTON)
        self.wait.until(lambda d: Urls.LOGIN not in d.current_url)

    def is_login_form_visible(self) -> bool:
        return (
            self.is_visible(AuthorizationPageLocators.EMAIL_INPUT)
            and self.is_visible(AuthorizationPageLocators.PASSWORD_INPUT)
            and self.is_visible(AuthorizationPageLocators.LOG_IN_BUTTON)
        )

    def is_on_login_page(self) -> bool:
        return Urls.LOGIN in self.get_current_url()