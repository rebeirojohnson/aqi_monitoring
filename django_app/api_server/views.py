from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .db_con import processQuery,engine
import requests as req
from bs4 import BeautifulSoup
import random
import datetime
from .models import *
import json
import numpy as np
from .pred import predict_aqi
import requests
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def livedataview(request):
	tasks = live_data.objects.all().order_by('-creation_time')
	serializer = Livedataserializer(tasks, many=True)
	return Response(serializer.data)

# @api_view(['GET'])
# def taskDetail(request, pk):
# 	tasks = Task.objects.get(id=pk)
# 	serializer = TaskSerializer(tasks, many=False)
# 	return Response(serializer.data)

@api_view(['POST'])
def taskDetail(request):
	data = request.data
	print(data)
	return Response("Sucessfully posted")


@api_view(['POST'])
def taskCreate(request):
	serializer = Livedataserializer(data=request.data)
	if serializer.is_valid():
		print("valid")
		serializer.save()
	else:
		print(serializer.errors)
		print("invalid")
	return Response("Sucess")

@api_view(['Get'])
def taskUpdate(request, data):
	# http://127.0.0.1:8000/api/task-update/%7B%22Name%22:%22API%22,%22AQI%22:980.0%7D/
	res = json.loads(data)
	serializer = TaskSerializer(data=res)
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['POST'])
def taskDelete(request):
	data = request.data
	print(data)

	return Response('Item succsesfully delete!')

@api_view(['POST'])
def create(request):
	data = request.data
	print(data)
	return HttpResponse('Added item')

@api_view(['GET'])
def student_list(request):
	dummy = Student_details.objects.all()
	serializer = Studentdetailsserializer(dummy, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def add_attendence(request):
	data = request.data
	tag_id=data['tagid']
	query = f"SELECT sd.usn,sd.name FROM public.api_server_student_details as sd  where student_id = '{tag_id}'"
	df = processQuery(query)
	if df.empty:
		return Response("Invalid card")
	
	usn  = df['usn'][0]
	name  = df['name'][0]
	json_string = '{"usn":"'+usn+'"}'
	json_string = json.loads(json_string)
	serializer = Attendance_serializer(data=json_string)
	if serializer.is_valid():
		print("valid")
		serializer.save()
		return Response(name)
	else:
		print(serializer.errors)
		print("invalid")
		return Response("Invalid card")

	
@api_view(['POST'])
def getdata(request):
	data = request.data
	date_string = data['date']
	new_date = date_string.split(" ")[0]
	date = int("".join(new_date.split("-")))
	print(date)
	aqi,data_array = predict_aqi(date=date)

	weather={
		"aqi":aqi,
		"pm":round(data_array[0]),
		"no":round(data_array[2]),
		"no2":round(data_array[3]),
		"ch4":round(data_array[4]),
		"so2":round(data_array[6])

	}
	return Response(weather)

@api_view(['GET'])
def get_today_weather(request):
	result = req.get(url="https://api.weatherapi.com/v1/current.json?key=971d434f39f1440d8be142810231803&q=13.08,74.98%20&aqi=nohttp://api.weatherapi.com/v1/current.json?key=971d434f39f1440d8be142810231803&q=mudbidri%20&aqi=no")
	weather_data = json.loads(result.content)

	name = weather_data['location']
	place = name['name']

	current_weather = weather_data['current']
	humidity = current_weather['humidity']

	temp_c = current_weather['temp_c']
	condition = current_weather['condition']

	text= condition['text']

	icon= condition['icon']

	now = datetime.datetime.now() # current date and time

	date_time = int(now.strftime("%Y%m%d"))
	print(type(date_time))
	aqi,weather = predict_aqi(date_time)
	# print(a,b)

	data = {
    "name": "Moodbidri",
    "aqi": aqi,
    "icon": icon,
    'text':"AQI",
    "pmsecond":round(weather[0]),
    "sosecond":round(weather[6]),
  }
	# return Response()
	return JsonResponse(data)

@api_view(['POST'])
def add_iot_weather(request):
	# {"light":"0.00","humidity":"63.00","temperature":"31.00","moisture":"666.00"}
	# {\"light\":\"0.00\",\"humidity\":\"63.00\",\"temperature\":\"31.00\",\"moisture\":\"666.00\"}
	data = request.data
	light = data['light']
	humidity = data['humidity']
	temperature = data['temperature']
	moisture = data['moisture']
	
	try:		
		telegram_chat_id = "@weather845173"

		telegram_bot_id = "bot6236663076:AAGct2VT2I3j9rsY9ja-KANqJbbSLhEHWB0"

		print(int(float(light)))
		if int(float(light)) == 1:
			message = f"The Present temprature is {temperature} and the humidity in Moodbidri is {humidity}\nThe Soil moisture is {moisture} and it is dark outside"
		else:
			message = f"The Present temprature is {temperature} and the humidity in Moodbidri is {humidity}\nThe Soil moisture is {moisture} and it is bright outside"

		teleurl = "https://api.telegram.org/"+telegram_bot_id+"/sendMessage"
		print(teleurl)
		data = {
			"chat_id": telegram_chat_id,
			"text": message
		}
		print(data)
		requests.post(teleurl, params=data)
		return JsonResponse({"message":"Sucess"}) 

	except Exception as e:
		print(e)
		return JsonResponse({"message":"Fail"}) 