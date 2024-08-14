from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse
from users.forms import UserLoginForm
from django.http import HttpResponseRedirect

def login(request):
    if request.method == 'POST': # Проверка типа метода
        form = UserLoginForm(data=request.POST) # Передача форме словаря данных из запроса
        if form.is_valid(): # Валидация данных полученных из POST запроса (у каждой формы есть такой метод )
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password) 
            # проверка в базе данных пользователя user 
            if user: # если найден в базе данных такой пользователь
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index')) # перенаправление пользователя после регистрации на главную страницу
    else: # Срабатывает только тогда, когда пользователь переходит на */user/login, то есть срабатывает GET-запрос
        form = UserLoginForm() 

    context =  {
        'title': 'Home - Авторизация',
        'form': form
    }
    
    return render(request, 'users/login.html', context)

def registration(request):
    context =  {
        'title': 'Home - Регистрация'
    }
    
    return render(request, 'users/registration.html', context)

def profile(request):
    context =  {
        'title': 'Home - Кабинет'
    }
    
    return render(request, 'users/profile.html', context)

def logout(request):
    context =  {
        'title': 'Home - Авторизация'
    }
    
    return render(request, '', context)