from django.contrib import admin
from django.urls import path
from API import views

urlpatterns = [
    path('', views.Compliment, name="home"),
    path('bodd', views.broadcast_sms, name ='broadcast_sms'),
   
]