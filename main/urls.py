from django.urls import path
from main import views


app_name = 'main' # namespace из app/urls.py

urlpatterns = [
    path('', views.index, name='index'), # name необходимо указать чтобы затем использовать в шаблонах
    path('about/', views.about, name='about'),
]