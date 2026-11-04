import os


class Urls:
    BASE = os.getenv(
        "BASE_URL",
        "https://foodgram-frontend-1.foodgram.education-services.ru",
    )
    HOME = "/"
    LOGIN = "/signin"
    SIGNUP = "/signup"
    RECIPES = "/recipes"
    RECIPES_CREATE = "/recipes/create"

