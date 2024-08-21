
from django.utils.http import urlencode
from django import template
from goods.models import Categories

register = template.Library()

@register.simple_tag()
def tag_categories():
    return Categories.objects.all()
# В Django существует два вида пользовательских тегов 
# Обычные и включающие

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs) # add new value/values or update current values
    return urlencode(query) # convert dict with GET-params (from request) to url (page=2&sort=desc)