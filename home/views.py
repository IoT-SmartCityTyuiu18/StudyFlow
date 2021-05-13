from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
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


