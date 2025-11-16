import requests

def test_check_cookie():
    url = "https://playground.learnqa.ru/api/homework_cookie"
    response = requests.get(url)

    cookies = response.cookies.get_dict()

    print(f"Cookies: {cookies}")

    expected_cookie_name = "HomeWork"
    expected_cookie_value = "hw_value"

    assert cookies is not None, f"Cookie '{expected_cookie_name}' not found"
    assert cookies.get(expected_cookie_name) == expected_cookie_value, f"Cookie '{expected_cookie_name}' has wrong value"