from django.urls import path
from app3.views import *

app_name='Best'

urlpatterns=[
    path('Warner/',Warner,name='Warner'),
]