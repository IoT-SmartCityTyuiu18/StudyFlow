from django.urls import path
from .views import *

urlpatterns = [
    path('', overview, name='overview'),
    path('profile', s_profile, name='profile'),
    path('courses', course, name='course'),
    path('calendar', calendar, name='calendar'),
    path('my_messages', messages, name='messages'),
    path('marks', marks, name='my_marks'),
]
