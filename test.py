import requests as req
# import 

# result = req.get(url="https://api.weatherapi.com/v1/current.json?key=971d434f39f1440d8be142810231803&q=13.08,74.98%20&aqi=nohttp://api.weatherapi.com/v1/current.json?key=971d434f39f1440d8be142810231803&q=mudbidri%20&aqi=no")
# weather_data = json.loads(result.content)

# name = weather_data['location']
# place = name['name']

# current_weather = weather_data['current']
# humidity = current_weather['humidity']

# temp_c = current_weather['temp_c']
# condition = current_weather['condition']

# text= condition['text']

# icon= condition['icon']


# data = {
# "name": place,
# "temperature": temp_c,
# "icon": icon,
# "text": text,
# "humidity":humidity,
# }

# print(data)

response = req.post("http://www.greedandfear.fun:9999/api/add_weather",json={"light":"1.00","humidity":"263.00","temperature":"31.00","moisture":"666.00"})
# response = req.post("http://127.0.0.1:8000/api/add_weather",json={"light":"1.00","humidity":"63.00","temperature":"31.00","moisture":"666.00"})