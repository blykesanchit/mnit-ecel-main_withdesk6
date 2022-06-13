from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello",request)

def experience(request):
     return render(request, "experience.html")

# def allcourses(request):
#     return render(request, 'allcourses.html',{'allcoursedata':allcoursedata})