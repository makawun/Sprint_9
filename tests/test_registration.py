import allure

from data.users import Users
from pages.authorization_page import AuthorizationPage
from pages.registration_page import RegistrationPage


@allure.feature("Создание аккаунта")
class TestRegistration:

    @allure.title("Успешная регистрация нового пользователя")
    def test_registration_success(self, driver):
        user = Users.unique()

        auth = AuthorizationPage(driver)
        auth.open()
        auth.click_create_account()

        reg = RegistrationPage(driver)
        reg.fill_form(user)
        reg.submit()

        assert auth.is_on_login_page()
        assert auth.is_login_form_visible()