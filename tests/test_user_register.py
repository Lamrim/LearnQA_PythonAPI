import random
import string

import allure

from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
import pytest

@allure.feature("User")
@allure.story("Register user")
class TestUserRegister(BaseCase):
    params = [
        "email",
        "password",
        "username",
        "firstName",
        "lastName"
    ]

    @allure.description("Success to register user")
    @allure.tag("positive")
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.description("Try to register user with existing email")
    @allure.tag("negative")
    def test_create_user_with_existing_email(self):
        email = "vinkotov@example.com"
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_status_code(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", \
            f"Unexpected response.content: {response.content}"

    @allure.description("Try to register user with invalid email")
    @allure.tag("negative")
    def test_create_user_with_invalid_email(self):
        data = self.prepare_registration_data("invalide_email.com")

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_status_code(response, 400)
        assert response.text == "Invalid email format"

    @allure.description("Try to register user without required params")
    @allure.tag("negative")
    @pytest.mark.parametrize("missing_param", params)
    def test_create_user_without_required_param(self, missing_param):
        data = self.prepare_registration_data()
        data.pop(missing_param)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_status_code(response, 400)
        assert response.text == f"The following required params are missed: {missing_param}"

    @allure.description("Try to register user with short username")
    @allure.tag("negative")
    def test_create_user_with_short_username(self):
        data = self.prepare_registration_data()
        data["username"] = "a"

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_status_code(response, 400)
        assert response.text == "The value of 'username' field is too short"

    @allure.description("Try to register user with long username")
    @allure.tag("negative")
    def test_create_user_with_long_username(self):
        data = self.prepare_registration_data()
        data["username"] = ''.join(random.choices(string.ascii_letters + string.digits, k=251))

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_status_code(response, 400)
        assert response.text == "The value of 'username' field is too long"


