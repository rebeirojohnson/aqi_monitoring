import requests

url = "http://139.59.64.29:9999/api/get-weather/"
url = "http://127.0.0.1:8000/api/get-weather/"

# data = requests.post(url=url,json={"date":"2022-11-06"})
data = requests.post(url=url,json={"date":"2023-03-30 22:28:46.356308"})

print(data.content)