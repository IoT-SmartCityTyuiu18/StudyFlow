import hashlib

from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User


def get_header_name(self):
    if self.first_name or self.last_name:
        return self.first_name + " " + self.last_name[:1] + "."
    return self.username

User.add_to_class("get_header_name",get_header_name)


class Class(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    GENDER = [('male', 'Мужской'), ('female', 'Женский')]
    DEGREE = [('bachelor', 'Бакалавриат'),
              ('specialty', 'Специалитет'),
              ('magistracy', 'Магистратура'),
              ('SSE', 'Среднее специальное'),
              ('postgraduate', 'Аспирантура')]

    # Personality data
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, null=True, blank=True)
    birth_date = models.DateField(default=timezone.now, null=True, blank=True)
    degree = models.CharField(max_length=100, choices=DEGREE, help_text='Current studying level')
    current_class = models.ForeignKey(Class, on_delete=models.CASCADE)

    # Profile data
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='static/avatars/', null=True, blank=True)

    def get_gender(self):
        return self.gender

    def __str__(self):
        return self.name + " " + self.patronymic
