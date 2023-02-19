from django.db import models

import datetime
# Create your models here.

class Weather(models.Model):
    Datetime = models.DateTimeField(auto_created=True)
    PM = models.FloatField()
    NO = models.FloatField()
    NO2 = models.FloatField()
    NOx = models.FloatField()
    CO = models.FloatField()
    SO2 = models.FloatField()
    O3 = models.FloatField()
    AQI = models.FloatField()

    def __str__(self):
        return self.title

class live_data(models.Model):
    Datetime = models.DateTimeField(auto_now=True)
    ch4 = models.FloatField()
    Coal = models.FloatField()
    CO = models.FloatField()
    Sulfur = models.FloatField()
    butane = models.FloatField()
    
 
    
class Student_details(models.Model):
    student_id = models.CharField(max_length=8,primary_key=True)
    Name = models.CharField(max_length=50)
    usn = models.CharField(max_length=10)
    phonenum = models.IntegerField()

    def __str__(self):
        return self.title
    
class Attendance_details(models.Model):
    sl_no = models.BigAutoField(primary_key=True)
    student_id = models.CharField(max_length=8)
    attendence_time = models.DateTimeField(auto_now=True)
