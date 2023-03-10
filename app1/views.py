from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Dhoni(request):
    return HttpResponse('<h1>MSD forever</h1>')
def Raina(request):
    return HttpResponse('<h1>Mr.IPL</h1>')
