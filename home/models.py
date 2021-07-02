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


class Subject(models.Model):
    TYPES = [('0', 'Зачет'), ('1', 'Экзамен'), ('2', 'Практика')]

    title = models.CharField(max_length=100)
    acad_hours = models.CharField(max_length=10)
    exam = models.CharField(max_length=15, choices=TYPES)

    def __str__(self):
        return self.title


class Course_work(models.Model):
    title = models.CharField(max_length=100)
    mark = models.IntegerField()

    def __str__(self):
        return self.title + ", " + str(self.mark)


class Stud_Mark(models.Model):
    MARKS = [('3', 'Удовлетворительно'), ('4', 'Хорошо'), ('5', 'Отлично')]
    SEMESTERS = [('1', '1, осенний'), ('2', '2, весенний')]

    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    subject = models.CharField(max_length=100)
    semester = models.CharField(max_length=50, choices=SEMESTERS)
    course_work = models.ForeignKey(Course_work, null=True, blank=True, on_delete=models.SET_NULL)
    mark = models.CharField(max_length=15, choices=MARKS)
    score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.subject + " " + self.mark


class Course(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(null=True, blank=True)
    href = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class Stud_course_progress(models.Model):
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)
    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    progress = models.IntegerField(default=0)

    def __str__(self):
        return self.course.name + " " + str(self.progress)


