from selenium.webdriver.common.by import By

class CreateRecipePageLocators:

    RECIPE_NAME_INPUT = (By.XPATH, ".//div[@class='styles_input__2Dg_j']/label[@class='styles_inputLabel__u_wTn']/input[@class='styles_inputField__3eqTj']")

    BREAKFAST_TAG = (By.XPATH, ".//div[@class='styles_checkboxGroup__MPxb8 styles_checkboxGroup__2SWIr']/div[2]/div[1]/button")
    LUNCH_TAG = (By.XPATH, ".//div[@class='styles_checkboxGroup__MPxb8 styles_checkboxGroup__2SWIr']/div[2]/div[2]/button")
    DINNER_TAG = (By.XPATH, ".//div[@class='styles_checkboxGroup__MPxb8 styles_checkboxGroup__2SWIr']/div[2]/div[3]/button")

    INGREDIENT_NAME_INPUT = (By.XPATH, ".//div[@class='styles_ingredientsInputs__1W-NV']/div/label[@class='styles_inputLabel__u_wTn']/input[1]")

    INGREDIENT_AMOUNT_INPUT = (By.XPATH, ".//div[@class='styles_ingredientsInputs__1W-NV']/div[2]//input[1]")

    ADD_INGREDIENT = (By.XPATH, ".//div[text()='Добавить ингредиент']")

    COOKING_TIME_INPUT = (By.XPATH, ".//div[@class='styles_cookingTime__2vRcp']//input[1]")

    DESCRIPTION_INPUT = (By.XPATH, ".//textarea[@class='styles_textareaField__1wfhC']")

    PHOTO_INPUT = (By.XPATH, ".//input[@type='file']")

    INGREDIENT_OPTION = (By.XPATH, ".//div[@class='styles_container__3ukwm']/div[1]")

    CREATE_BUTTON = (By.XPATH, ".//button[text()='Создать рецепт']")