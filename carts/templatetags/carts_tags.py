from django import template
from carts.models import Cart

register = template.Library() # декоратор для тега

@register.simple_tag()
def user_cart(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user) 
# по полю user находит соответствие из запроса
# то есть находим все продукты, выбранные пользователем в корзину
