import requests

response1 = requests.get("https://playground.learnqa.ru/api/compare_query_type")
print(f"1: { response1.text}")

response2 = requests.head("https://playground.learnqa.ru/api/compare_query_type", data={"method": "HEAD"})
print(f"2: {response2.text}")

response3 = requests.post("https://playground.learnqa.ru/api/compare_query_type", data={"method": "POST"})
print(f"3: {response3.text}")

methods = ["POST", "GET", "PUT", "DELETE"]

def check(method, params_method, text):
    succeed_text = '{"success":"!"}'
    if method == params_method and text != succeed_text or method != params_method and text == succeed_text:
        print(f"4: Ошибочный ответ сервера {text} при вызове метода {method} с параметром {params_method}")
        return

for method in methods:
    for params_method in methods:
        if method == "GET":
            response4 = requests.get("https://playground.learnqa.ru/api/compare_query_type", params={"method": params_method})
            check(method, params_method, response4.text)
        elif method == "POST":
            response4 = requests.post("https://playground.learnqa.ru/api/compare_query_type", data={"method": params_method})
            check(method, params_method, response4.text)
        elif method == "PUT":
            response4 = requests.put("https://playground.learnqa.ru/api/compare_query_type", data={"method": params_method})
            check(method, params_method, response4.text)
        elif method == "DELETE":
            response4 = requests.delete("https://playground.learnqa.ru/api/compare_query_type", data={"method": params_method})
            check(method, params_method, response4.text)






