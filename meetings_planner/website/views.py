from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def welcome(request):
    return HttpResponse('<h1>Welcome to the Meeting Planner</h1>')

def date(request):
    return HttpResponse('This page was served at ' + str(datetime.now()))

def about(request):
    return HttpResponse("This is me here! Halleluyah")
