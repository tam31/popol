from django.db import models

# Create your models here.

#이쪽에 모델추가
#태민 테스트

# class Input(models.Model): # 처음 입력 모델
#     user_id = models.OneToOneField(User, on_delete=models.CASCADE)
#     tag = models.ManyToManyField(Tag, blank=True)
#     period = models.IntegerField()
#     area = models.CharField(max_length=20)
#
# class Tag(models.Model): # 태그 모델
#     name = models.CharField(max_length=12)
#     value = models.FloatField()
#
# class Tour(models.Model): # 관광지 모델
#     name = models.CharField(max_length=30)
#     content_time = models.IntegerField()
#     image = models.URLField()
#     x_value = models.FloatField()
#     y_value = models.FloatField()
#
# class Restaurant(models.Model): # 식당 모델
#     name = models.CharField(max_length=30)
#     content_time = models.IntegerField()
#     image = models.URLField()
#     x_value = models.FloatField()
#     y_value = models.FloatField()
#
# class Stay(models.Model): # 숙소 모델
#     name = models.CharField(max_length=30)
#     content_time = models.IntegerField()
#     image = models.URLField()
#     x_value = models.FloatField()
#     y_value = models.FloatField()
#
# class Schedule(models.Model): # 일정리스트 모델
#     user_id = models.OneToOneField(User, on_delete=models.CASCADE)
#     tag = models.ManyToManyField(Tag, blank=True)
#     tour = models.ManyToManyField(Tour, blank=True)
#     restaurant = models.ManyToManyField(Restaurant, blank=True)
#     stay = models.ManyToManyField(Stay, blank=True)
