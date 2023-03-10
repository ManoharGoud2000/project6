from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Warner(request):
    return HttpResponse('<h1><marquee>Jai Warner Mowa</marquee></h1>')