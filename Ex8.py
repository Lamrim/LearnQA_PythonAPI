import requests
import time

url = "https://playground.learnqa.ru/ajax/api/longtime_job"

response = requests.get(url)
token = response.json()["token"]
interval = response.json()["seconds"]

response = requests.get(url, params={"token": token})
response_data = response.json()
if response_data["status"] == "Job is NOT ready":
    print(f"job status is correct, waiting for {interval} seconds")
    time.sleep(interval)
    response = requests.get(url, params={"token": token})
    response_data = response.json()
    if response_data["status"] == "Job is ready" and "result" in response_data:
        print(f"ok, result = {response_data['result']}")
    else: print("status is incorrect or result is none")
else: print("status is incorrect")