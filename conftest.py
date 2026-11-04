import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data.users import Users
from pages.authorization_page import AuthorizationPage
from pages.registration_page import RegistrationPage

SELENOID_URL = os.getenv("SELENOID_URL", "http://localhost:4444/wd/hub")


@pytest.fixture
def driver():
    options = Options()
    options.set_capability(
        "selenoid:options",
        {
            "enableVNC": True,
            "enableVideo": False,
            "screenResolution": "1920x1080x24",
        },
    )
    driver = webdriver.Remote(command_executor=SELENOID_URL, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def registered_user(driver) -> dict:
    user = Users.unique()

    auth = AuthorizationPage(driver)
    auth.open()
    auth.click_create_account()

    reg = RegistrationPage(driver)
    reg.fill_form(user)
    reg.submit()

    assert auth.is_on_login_page(), "Регистрация не привела на страницу авторизации"
    return user


@pytest.fixture
def authorized_user(driver, registered_user) -> dict:
    AuthorizationPage(driver).login(
        registered_user["username"], registered_user["password"]
    )
    return registered_user