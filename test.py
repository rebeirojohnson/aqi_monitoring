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

# response = req.post("http://www.greedandfear.fun:9999/api/add_weather",json={"light":"1.00","humidity":"263.00","temperature":"31.00","moisture":"666.00"})
# response = req.post("http://127.0.0.1:8000/api/add_weather",json={"light":"1.00","humidity":"63.00","temperature":"31.00","moisture":"666.00"})
import random
from sqlalchemy import create_engine,text

test_url = "postgresql+psycopg2://johnson:tMl2l7rHO6dQcP1xVBlmF2Wv3n0uBIcJ@dpg-cftdlharrk0c835ilaj0-a.oregon-postgres.render.com:5432/test_db"

engine = create_engine(test_url)

for exam_id in [1,2,3,4,5,6]:
    for usn in ['4DM19EC036','4DM19EC018','4DM19EC047']:
        marks = random.choice(range(1,30))
        query = f"""INSERT INTO public.student_perfomance(
	 exam_id, usn, marks_scored, attendance_status)
	VALUES ({exam_id},'{usn}',{marks},{True});"""
        engine.execute(text(query))
        

