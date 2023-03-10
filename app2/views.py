from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Rohit(request):
    return HttpResponse('<marquee><h1>Rohit is best Opening Batsman in the World</h1></marquee>')