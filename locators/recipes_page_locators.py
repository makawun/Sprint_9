from selenium.webdriver.common.by import By


class RecipesPageLocators:
    LOGIN_BUTTON = (By.XPATH, ".//a[text()='Войти']")
    LOGOUT_BUTTON = (By.XPATH, ".//a[text()='Выход']")
    CREATE_RECIPE_LINK = (By.XPATH, ".//a[@href='/recipes/create']")
    RECIPE_TITLE = (By.XPATH, ".//h1[contains(@class, 'styles_single-card__title')]")