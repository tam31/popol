from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
# Create your models here.
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Tag(models.Model): # 태그 모델
    name = models.CharField(max_length=12)
    def __str__(self):
        return self.name



class Input(models.Model): # 처음 입력 모델
    id = models.AutoField(primary_key=True)
    startperiod = models.DateField(null=True)
    endperiod = models.DateField(null=True)
    startime = models.TimeField(null=True)
    tag = models.ManyToManyField(Tag, blank=True)
    area = models.CharField(max_length=20,default='')


class Tour(models.Model): # 관광지 모델
    name = models.CharField(max_length=30)
    tag = models.ManyToManyField(Tag, blank=True)
    tourTime = models.FloatField(null=True)
    tourLatitude = models.FloatField(blank=True)
    tourLongitude = models.FloatField(blank=True)
    tour_url = models.URLField('관광지 URL', max_length=400, blank=True, null=True, default='')
    visitCnt = models.IntegerField(default=0)

    def json(self):
        return {
            "name": self.name,
            "Time": self.tourTime,
            "Latitude": self.tourLatitude,
            "Longitude": self.tourLongitude,
            "url": self.tour_url,
            "visitCnt": self.visitCnt
        }
    def __str__(self):
        return self.name

class Restaurant(models.Model): # 식당 모델
    name = models.CharField(max_length = 20)
    restaurantTime = models.IntegerField(null=True)
    restaurantLatitude = models.FloatField(blank=True)
    restaurantLognitude = models.FloatField(blank=True)
    restaurant_url = models.URLField('식당 URL', max_length=400, blank=True,null=True,default='')
    visitCnt = models.IntegerField(default=0)

    def json(self):
        return {
            "name": self.name,
            "Time": self.restaurantTime,
            "Latitude": self.restaurantLatitude,
            "Longitude": self.restaurantLognitude,
            "url": self.restaurant_url,
            "visitCnt": self.visitCnt
        }

    def __str__(self):
        return self.name

class Stay(models.Model): # 숙소 모델
    name = models.CharField(max_length=20)
    stayLatitude = models.FloatField(blank=True)
    stayLognitude = models.FloatField(blank=True)
    stay_url = models.URLField('숙소 UR', max_length=400, blank=True,null=True, default='')
    visitCnt = models.IntegerField(default=0)

    def json(self):
        return {
            "name": self.name,
            "Latitude": self.stayLatitude,
            "Longitude": self.stayLognitude,
            "url": self.stay_url,
            "visitCnt": self.visitCnt
        }

    def __str__(self):
        return self.name

class Schedule(models.Model): # 일정리스트 모델
    user_id = models.CharField(max_length = 20)
    tag = models.ManyToManyField(Tag, blank=True)
    schedule = models.TextField()


    def __str__(self):
        return self.user_id
