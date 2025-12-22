import datetime
import os
from requests import Response


class Logger:
    file_name = f"logs/log_{datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')}.log"

    @classmethod
    def _write_log(cls, data: str):
        os.makedirs(os.path.dirname(cls.file_name), exist_ok=True)
        with open(cls.file_name, "a", encoding="utf-8") as logger_file:
            logger_file.write(data)

    @classmethod
    def add_request(cls, url: str, data: dict, headers: dict, cookies: dict, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        log_data = "\n-------\n"
        log_data += f"Test: {test_name}\n"
        log_data += f"Time: {datetime.datetime.now()}\n"
        log_data += f"Request method: {method}\n"
        log_data += f"Request URL: {url}\n"
        log_data += f"Request data: {data}\n"
        log_data += f"Request headers: {headers}\n"
        log_data += f"Request cookies: {cookies}\n"
        log_data += "\n"

        cls._write_log(log_data)

    @classmethod
    def add_response(cls, response: Response):
        cookies_as_dict = dict(response.cookies)
        headers_as_dict = dict(response.headers)

        log_data = f"Response code: {response.status_code}\n"
        log_data += f"Response text: {response.text}\n"
        log_data += f"Response headers: {headers_as_dict}\n"
        log_data += f"Response cookies: {cookies_as_dict}\n"
        log_data += "\n-------\n"

        cls._write_log(log_data)