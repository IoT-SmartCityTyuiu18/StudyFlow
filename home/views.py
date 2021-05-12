from django.shortcuts import render
from django.views import generic


#class LoginView(generic.ListView):
#    model = student


def overview(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    return render(
        request,
        'overview_page.html',
        context={},
    )

