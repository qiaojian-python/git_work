# from django.contrib import admin
from django.urls import path
from api.views import Demo,UserAPIView
from rest_framework import throttling

urlpatterns = [
    path('demo/',Demo.as_view()),
    path('user/',UserAPIView.as_view()),
]