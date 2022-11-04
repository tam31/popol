from django.urls import path

from . import views

app_name = 'community'

urlpatterns = [
    path('', views.Home, name='user'),
    #path('create', views.Create, name='input'),
    path('create', views.Date, name='date'),
    path('create/amend', views.Amend, name='amend'),
    path('create/amend/check', views.Check, name='check')

]