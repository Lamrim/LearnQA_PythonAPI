import allure

from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests

@allure.feature("User")
@allure.story("Delete user")
class TestUserDelete(BaseCase):
    def test_user_with_id_2_delete(self):
        response1 = MyRequests.delete("/user/2")

        Assertions.assert_status_code(response1, 400)

    @allure.description("Successful delete new user")
    @allure.tag("positive")
    def test_create_and_delete_user_successfully(self):
        #REGISTER AND LOGIN
        user_id, auth_sid, token = self.create_and_login_user()

        #DELETE
        response1 = MyRequests.delete(f"/user/{user_id}",
                                            headers={"x-csrf-token": token},
                                            cookies={"auth_sid": auth_sid})

        Assertions.assert_status_code(response1, 200)

        #GET
        response2 = MyRequests.get(f"/user/{user_id}",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid})

        Assertions.assert_status_code(response2, 404)

    @allure.description("Try to delete user as other user")
    @allure.tag("negative")
    def test_delete_user_as_other_user(self):
        #REGISTER AND LOGIN
        user_to_delete_id1, auth_sid1, token1 = self.create_and_login_user()

        user_to_delete_id2, auth_sid2, token2 = self.create_and_login_user()

        #DELETE
        response_delete = MyRequests.delete(f"/user/{user_to_delete_id1}",
                                            headers={"x-csrf-token": token2},
                                            cookies={"auth_sid": auth_sid2})

        Assertions.assert_status_code(response_delete, 400)