
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def course_home(request):
    return render(request, 'course_home.html')

def desktop_18(request):
    return render(request, 'desk18.html')