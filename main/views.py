from django.http import HttpResponse
from django.shortcuts import render

def index(request): # представления или контроллеры
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME'
        }
    return render(request, 'main/index.html', context) # так как в templates будет искать автоматически. поэтому main/index.html, весь context передается через render в html


def about(request): # представления или контроллеры
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст какой-то'
        }
    return render(request, 'main/about.html', context) 
