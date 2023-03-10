from django.urls import path
from app2.views import *

app_name='Everything'

urlpatterns=[
    path('Rohit/',Rohit,name='Rohit'),
]