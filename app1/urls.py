from django.urls import path
from app1.views import *

app_name='Something'

urlpatterns=[
    path('Dhoni/',Dhoni,name='Dhoni'),
    path('Raina',Raina,name='Raina'),

]