from requests import Response
import json

class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_msg):
        try:
           response_as_dict = response.json()
        except json.JSONDecodeError:
           assert False, f"Response is not a valid json. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response doesn't have key '{name}'"
        assert response_as_dict[name] == expected_value, error_msg

    @staticmethod
    def assert_json_value_by_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not a valid json. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response doesn't have key '{name}'"

    @staticmethod
    def assert_status_code(response: Response, expected_status_code):
       assert response.status_code == expected_status_code, f"Unexpected status code: expected:{expected_status_code}, \
                got: {response.status_code}"



