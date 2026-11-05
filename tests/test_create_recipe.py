from pathlib import Path

import allure

from data.recipes import Recipes
from pages.create_recipe_page import CreateRecipePage
from pages.recipes_page import RecipesPage

ASSETS_DIR = Path(__file__).parent.parent / "assets"


@allure.feature("Создание рецепта")
class TestCreateRecipe:

    @allure.title("Успешное создание рецепта")
    def test_create_recipe_success(self, driver, authorized_user):
        recipes = RecipesPage(driver)
        recipes.go_to_create_recipe()

        recipe = Recipes.unique()
        page = CreateRecipePage(driver)
        page.fill_recipe(recipe, tag="lunch")
        page.upload_photo(str(ASSETS_DIR / "test_image.png"))
        page.submit()

        assert recipes.is_recipe_title_visible()
        assert recipe["name"] == recipes.get_recipe_title_text()