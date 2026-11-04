from random import randint


class Recipes:
    INGREDIENT = "молоко"
    AMOUNT = "100"
    COOKING_TIME = "10"
    DESCRIPTION = "Тестовое описание рецепта"

    @staticmethod
    def unique() -> dict:
        suffix = randint(100_000_000, 999_999_999)
        return {
            "name": f"Рецепт {suffix}",
            "ingredient": Recipes.INGREDIENT,
            "amount": Recipes.AMOUNT,
            "cooking_time": Recipes.COOKING_TIME,
            "description": Recipes.DESCRIPTION,
        }