from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
# from .db_con import processQuery,engine
import requests as req
from bs4 import BeautifulSoup
from .models import *
import json
from .pred import predict_aqi
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
	date = data['date']
	aqi = predict_aqi(date=date)
	weather={
		"aqi":aqi
	}
	return Response(weather)

@api_view(['GET'])
def verify(request):
	result = req.get(url="https://api.weatherapi.com/v1/current.json?key=971d434f39f1440d8be142810231803&q=13.08,74.98%20&aqi=nohttp://api.weatherapi.com/v1/current.json?key=971d434f39f1440d8be142810231803&q=mudbidri%20&aqi=no")
	# soup = BeautifulSoup(result.content, 'lxml')
	# text_json = soup.text
	# data = json.loads(text_json)
	weather_data = json.loads(result.content)

	name = weather_data['location']
	place = name['name']

	current_weather = weather_data['current']
	humidity = current_weather['humidity']

	temp_c = current_weather['temp_c']
	condition = current_weather['condition']

	text= condition['text']

	icon= condition['icon']


	data = {
    "name": place,
    "temperature": temp_c,
    "icon": icon,
    "text": text,
    "humidity":humidity,
  }
	return Response(f"name:{place}")
	# return JsonResponse(data)



