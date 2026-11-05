from random import randint


class Users:
    FIRST_NAME = "Test"
    LAST_NAME = "User"
    PASSWORD = "Str0ng!Passw0rd#2024"

    @staticmethod
    def unique() -> dict:
        suffix = randint(100_000_000, 999_999_999)
        return {
            "first_name": Users.FIRST_NAME,
            "last_name": Users.LAST_NAME,
            "username": f"user{suffix}",
            "email": f"test{suffix}@yandex.ru",
            "password": Users.PASSWORD,
        }