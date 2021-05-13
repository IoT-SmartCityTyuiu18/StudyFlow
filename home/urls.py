from django.urls import path
from .views import *

urlpatterns = [
    path('', overview, name='overview'),
    path('courses', course, name='course'),
    path('calendar', calendar, name='calendar'),
    path('my_messages', messages, name='messages'),
]
