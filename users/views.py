from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.urls import reverse
from carts.models import Cart
from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm

def login(request):
    if request.method == 'POST': # Проверка типа метода
        form = UserLoginForm(data=request.POST) # Передача форме данных введенных пользователем
        if form.is_valid(): # Валидация данных полученных из POST запроса (у каждой формы есть такой метод )
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password) 

            session_key = request.session.session_key # нужно для сохранения корзины не авторизованного пользователя

            # проверка в базе данных пользователя user 
            if user: # если найден в базе данных такой пользователь
                auth.login(request, user) # меняется сессионный ключ и файлы куки при авторизации, Django автоматически при авторизации генерирует свой ключ
                messages.success(request, f"{username} Вы успешно авторизовались!")

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user) # привязываем user с корзинами с помощью session_key

                redirect_page = request.POST.get('next', None) # при user/profile, если не залогинен
                if redirect_page and redirect_page != reverse('user:logout'):
                    return redirect(request.POST.get('next'))
                return redirect(reverse('main:index')) # перенаправление пользователя после регистрации на главную страницу
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

            session_key = request.session.session_key

            user = form.instance 
            # берем экземпляр модели User 
            # (то есть все поля с данными введенные пользователем)
            auth.login(request, user) # и дополнительно авторизуем его
            messages.success(request, f"{user.username} Вы успешно зарегистрировались!")

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)

            return redirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
    context =  {
        'title': 'Home - Регистрация',
        'form': form
    }
    
    return render(request, 'users/registration.html', context)


@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid(): # Проверяем данные на валидность
            form.save() # Сохраняем изменения если они есть
            return redirect(reverse("user:profile"))
    else:
        form = ProfileForm(instance=request.user) # указываем с помощью instance для какого пользователя


    context =  {
        'title': 'Home - Кабинет',
        'form': form
    }
    
    return render(request, 'users/profile.html', context) 
    # templates не нужен, автоматически уже включен


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, f"{request.user. username} Вы вышли из аккаунта!")
    return redirect(reverse('main:index'))



def users_cart(request): # корзина для пользователя
    return render(request, 'users/users_cart.html')