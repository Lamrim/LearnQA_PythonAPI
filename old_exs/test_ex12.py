import requests

def test_check_header():
    url = "https://playground.learnqa.ru/api/homework_header"
    response = requests.get(url)

    headers = response.headers

    print(f"Headers: {headers}")

    expected_header_name = "x-secret-homework-header"
    expected_header_value = "Some secret value"

    assert expected_header_name in headers, f"Header '{expected_header_name}' not found"
    assert headers.get(expected_header_name) == expected_header_value, f"Header '{expected_header_name}' has wrong value"