from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestUserEdit(BaseCase):

    def edit_user(self, user_id, auth_sid=None, token=None, data=None):
        headers = {"x-csrf-token": token}
        cookies = {"auth_sid": auth_sid}

        return MyRequests.put(f"/user/{user_id}", headers=headers, cookies=cookies, data=data)

    def test_edit_just_created_user(self):
        user_id, auth_sid, token = self.create_and_login_user()

        new_name = "New name"
        response = self.edit_user(user_id, auth_sid, token, {"firstName": new_name})

        Assertions.assert_status_code(response, 200)

        response_get = MyRequests.get(f"/user/{user_id}",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_by_name(response_get, "firstName", new_name, "Wrong name")

    def test_edit_user_without_authorization(self):
        user_id, auth_sid, token = self.create_and_login_user()
        new_name = "New name"

        response = self.edit_user(user_id, data={"firstName": new_name})

        Assertions.assert_status_code(response, 400)

    def test_edit_as_other_user(self):
        user_id, auth_sid, token = self.create_and_login_user()

        other_user_id = 2
        new_name = "New name"

        response = self.edit_user(other_user_id, auth_sid, token, {"firstName": new_name})

        Assertions.assert_status_code(response, 400)

    def test_edit_with_invalid_email(self):
        user_id, auth_sid, token = self.create_and_login_user()
        invalid_email = "invalidemail.com"
        response = self.edit_user(user_id, auth_sid, token, {"email": invalid_email})

        Assertions.assert_status_code(response, 400)

    def test_edit_with_short_name(self):
        user_id, auth_sid, token = self.create_and_login_user()
        short_name = "M"
        response = self.edit_user(user_id, auth_sid, token, {"firstName": short_name})

        Assertions.assert_status_code(response, 400)
