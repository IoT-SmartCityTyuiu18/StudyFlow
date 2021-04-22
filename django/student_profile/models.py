from django.db import models

# Create your models here.


class StudProfile(models.Model):
    email = models.EmailField()
    avatar = models.ImageField()

    def __str__(self):
        return self.email


class Grade(models.Model):
    name = models.CharField(max_length=30, help_text="Short name of achievement")
    courses = models.FloatField(max_length=11, help_text="Number of courses for full education program")

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)
    birth_date = models.DateField()
    fk_grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    fk_profile = models.ForeignKey(StudProfile, on_delete=models.CASCADE)
    avg_mark = models.FloatField(max_length=3, help_text="Exams average rating")
    group = models.CharField(max_length=30, help_text="Student group")
    role = models.CharField(max_length=50, help_text="Choosing role of student")

    def __str__(self):
        return "%s %s" % (self.name, self.surname)

