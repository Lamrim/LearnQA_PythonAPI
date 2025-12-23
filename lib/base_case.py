import json
from datetime import datetime
from requests import Response
from lib.my_requests import MyRequests


class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Cannot find cookie {cookie_name} in the last response"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, header_name):
        assert header_name in response.headers, f"Cannot find header {header_name} in the last response"
        return response.headers[header_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in json format. Response text is {response.text}"

        assert name in response_as_dict, f"Response json does not contain key '{name}'"

        return response_as_dict[name]

    def prepare_registration_data(self, email=None):
        if email is None:
            base_part = "learnqa"
            domain = "example.com"
            random_part = datetime.now().strftime("%Y%m%d%H%M%S")
            email = f"{base_part}-{random_part}@{domain}"
        return {
            "username": "learnqa",
            "firstName": "learnqa",
            "lastName": "learnqa",
            "email": email,
            "password": "123"
        }

    def create_and_login_user(self, custom_data=None):
        #REGISTER
        register_data = custom_data or self.prepare_registration_data()
        response = MyRequests.post("/user/", data=register_data)
        assert response.status_code == 200, f"User creation failed: {response.text}"
        user_id = self.get_json_value(response, "id")

        #LOGIN
        login_data = {"email": register_data["email"], "password": register_data["password"]}
        login_response = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(login_response, "auth_sid")
        token = self.get_header(login_response, "x-csrf-token")

        return user_id, auth_sid, token
