from selenium.webdriver.common.by import By

class AuthorizationPageLocators:
    
    CREATE_ACCOUNT_BUTTON = (By.XPATH, ".//a[@href='/signup']")

    EMAIL_INPUT = (By.XPATH, ".//input[@name='email']")

    PASSWORD_INPUT = (By.XPATH, ".//input[@name='password']")

    LOG_IN_BUTTON = (By.XPATH, ".//button[text()='Войти']")