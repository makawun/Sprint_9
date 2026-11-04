from pages.base_page import BasePage
from locators.create_recipe_page_locators import CreateRecipePageLocators


class CreateRecipePage(BasePage):
    TAGS = {
        "breakfast": CreateRecipePageLocators.BREAKFAST_TAG,
        "lunch": CreateRecipePageLocators.LUNCH_TAG,
        "dinner": CreateRecipePageLocators.DINNER_TAG,
    }

    def fill_recipe(self, recipe: dict, tag: str = "breakfast"):
        self.fill(CreateRecipePageLocators.RECIPE_NAME_INPUT, recipe["name"])
        self.click(self.TAGS[tag])

        self.fill(CreateRecipePageLocators.INGREDIENT_NAME_INPUT, recipe["ingredient"])
        self.click_when_visible(CreateRecipePageLocators.INGREDIENT_OPTION)

        self.fill(CreateRecipePageLocators.INGREDIENT_AMOUNT_INPUT, recipe["amount"])
        self.click(CreateRecipePageLocators.ADD_INGREDIENT)

        self.fill(CreateRecipePageLocators.COOKING_TIME_INPUT, recipe["cooking_time"])
        self.fill(CreateRecipePageLocators.DESCRIPTION_INPUT, recipe["description"])

    def upload_photo(self, file_path: str):
        self.upload_file(CreateRecipePageLocators.PHOTO_INPUT, file_path)

    def submit(self):
        self.click(CreateRecipePageLocators.CREATE_BUTTON)
        self.wait.until(
            lambda d: "/recipes/create" not in d.current_url
            and "/recipes/" in d.current_url
        )