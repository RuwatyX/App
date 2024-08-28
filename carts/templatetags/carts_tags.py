from django import template
from carts.utils import get_user_carts
register = template.Library() # декоратор для тега

@register.simple_tag()
def user_cart(request):
    return get_user_carts(request) 
# по полю user находит соответствие из запроса
# то есть находим все продукты, выбранные пользователем в корзину
