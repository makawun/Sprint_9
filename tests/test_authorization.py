import allure

from pages.authorization_page import AuthorizationPage
from pages.recipes_page import RecipesPage


@allure.feature("Авторизация")
class TestAuthorization:

    @allure.title("Успешная авторизация зарегистрированного пользователя")
    def test_login_success(self, driver, registered_user):
        recipes = RecipesPage(driver)
        recipes.open()
        recipes.click_login_link()

        AuthorizationPage(driver).login(
            registered_user["username"], registered_user["password"]
        )

        assert recipes.is_on_home_page()
        assert recipes.is_logout_visible()