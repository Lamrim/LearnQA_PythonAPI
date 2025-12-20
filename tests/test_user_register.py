from datetime import datetime

import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserRegister(BaseCase):
    url = "https://playground.learnqa.ru/api/user/"

    def setup_method(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%Y%m%d%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"

    def test_create_user_sucessfully(self):
        data = {
            "username": "learnqa",
            "firstName": "learnqa",
            "lastName": "learnqa",
            "email": self.email,
            "password": "123"
        }

        response = requests.post(self.url, data=data)

        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_value_by_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = "vinkotov@example.com"
        data = {
            "username": "learnqa",
            "firstName": "learnqa",
            "lastName": "learnqa",
            "email": email,
            "password": "123"
        }

        response = requests.post(self.url, data=data)

        Assertions.assert_status_code(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", \
            f"Unpected response.content: {response.content}"


