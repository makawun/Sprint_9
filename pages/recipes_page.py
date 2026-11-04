from pages.base_page import BasePage
from locators.recipes_page_locators import RecipesPageLocators
from data.urls import Urls


class RecipesPage(BasePage):
    def open(self):
        super().open(Urls.HOME)

    def click_login_link(self):
        self.click(RecipesPageLocators.LOGIN_BUTTON)

    def go_to_create_recipe(self):
        self.click(RecipesPageLocators.CREATE_RECIPE_LINK)

    def is_logout_visible(self) -> bool:
        return self.is_visible(RecipesPageLocators.LOGOUT_BUTTON)

    def is_on_home_page(self) -> bool:
        return Urls.LOGIN not in self.get_current_url()

    def is_recipe_title_visible(self) -> bool:
        return self.is_visible(RecipesPageLocators.RECIPE_TITLE)

    def get_recipe_title_text(self) -> str:
        return self.find(RecipesPageLocators.RECIPE_TITLE).text