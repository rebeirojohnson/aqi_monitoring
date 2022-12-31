from django.db import models

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

class Testing(models.Model):
    Name = models.CharField(max_length=100)
    AQI = models.FloatField()
    
    def __str__(self):
        return self.title