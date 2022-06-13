
from urllib import request
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.course_home),
    path('desk18/',views.desktop_18),
]
