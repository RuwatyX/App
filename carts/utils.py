from carts.models import Cart

    
def get_user_carts(request):
        if request.user.is_authenticated:
            return Cart.objects.filter(user=request.user)
        if not request.session.session_key: # Срабатывает для не авторизованных пользователей
              request.session.create() # создаем session_key для тех у кого нет его
        return Cart.objects.filter(session_key=request.session.session_key)