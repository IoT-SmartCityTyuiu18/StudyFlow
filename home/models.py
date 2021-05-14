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


class Study_program(models.Model):
    code = models.CharField(max_length=8)
    title = models.CharField(max_length=100)

    def get_full_title(self):
        return self.code + ": " + self.title

    def __str__(self):
        return self.code + " " + self.title


class Class(models.Model):
    title = models.CharField(max_length=50, unique=True)
    St_program = models.ForeignKey(Study_program, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Institute(models.Model):
    name = models.CharField(max_length=100, unique=True)
    adress = models.CharField(max_length=200)
    # image = models.ImageField(upload_to='static/inst_img/', null=True, blank=True)
    # coordinates = models.CharField(max_length=100)

    def __str__(self):
        return self.name


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
    phone = models.CharField(max_length=12, null=True, blank=True)
    record_book = models.CharField(max_length=15, null=True, blank=True)
    degree = models.CharField(max_length=100, choices=DEGREE, help_text='Current studying level')
    current_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    institute = models.ForeignKey(Institute, null=True, on_delete=models.SET_NULL)

    # Profile data
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='static/avatars/', null=True, blank=True)

    def get_gender(self):
        return self.gender

    def __str__(self):
        return self.name + " " + self.patronymic
