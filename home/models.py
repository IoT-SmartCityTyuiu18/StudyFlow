import hashlib

from django.db import models
from django.utils import timezone
from django import forms


# Create your models here.
class Class(models.Model):
    title = models.CharField(max_length=50, unique=True)


class Student(models.Model):
    GENDER = [('male', 'Male'), ('female', 'Female')]
    DEGREE = [('bachelor', 'Bachelor'),
              ('specialty', 'Specialty'),
              ('magistracy', 'Magistracy'),
              ('SSE', 'secondary special'),
              ('postgraduate', 'Postgraduate')]

    # Personality data
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER)
    birth_date = models.DateField(default=timezone.now)
    degree = models.CharField(max_length=100, choices=DEGREE, help_text='Current studying level')
    current_class = models.ForeignKey(Class, on_delete=models.CASCADE)

    # Profile data
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True, help_text='Name uses on authorization page')
    password = models.CharField(max_length=30)
    avatar = models.ImageField()


