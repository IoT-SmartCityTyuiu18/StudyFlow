from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *


@login_required
def overview(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    return render(
        request,
        'overview_page.html',
        context={},
    )


def course(request):
    return render(
        request,
        'course_page.html',
        context={},
    )


def calendar(request):
    return render(
        request,
        'calendar_page.html',
        context={},
    )


def messages(request):
    return render(
        request,
        'message_page.html',
        context={},
    )
