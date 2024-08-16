from re import M
from django.shortcuts import redirect, render
from django.contrib import auth
from django.urls import reverse
from users.forms import UserLoginForm, UserRegistrationForm
from django.http import HttpResponseRedirect

def login(request):
    if request.method == 'POST': # Проверка типа метода
        form = UserLoginForm(data=request.POST) # Передача форме данных введенных пользователем
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
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST) # Форму заполняем данными из словаря
        if form.is_valid():
            form.save() # заносим данные введенные пользователем из формы в таблицу
            user = form.instance 
            # берем экземпляр модели User 
            # (то есть все поля с данными введенные пользователем)
            auth.login(request, user) # и дополнительно авторизуем его
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
    context =  {
        'title': 'Home - Регистрация',
        'form': form
    }
    
    return render(request, 'users/registration.html', context)

def profile(request):
    context =  {
        'title': 'Home - Кабинет'
    }
    
    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))