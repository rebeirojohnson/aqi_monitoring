from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Livedataserializer

from .models import *
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
	return Response("Data added successfully")


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
def view(request):
	dummy = {"data":[{'name':'Johnson','id':'4dm19ec036'},{'name':'Vaibhav','id':'4dm19ec047'},{'name':'Manju','id':'4dm19ec018'},{'name':'Test','id':'4dm19ec420'}]}
	return JsonResponse(dummy)
	



