from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, get_list_or_404
from goods.models import Categories, Products
from goods.utils import q_search


def catalog(request, category_slug=None):
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None) # результат поиска

    if category_slug == 'all':
        goods = Products.objects.all()
    elif query: 
        goods = q_search(query=query)
    else:
        goods = Products.objects.filter(category__slug=category_slug)
        if not goods:
            raise Http404('Empty page!')
        # именно этот метод, потому что category__slug=category_slug может быть несколько
        # и вызовется исключение MultipleObjectsReturned если другой метод

    if on_sale:
        goods = goods.filter(discount__gt=0)
    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)


    paginator = Paginator(goods, 3) # объект пагинатор, 3 объекта модели Products на страницу
    current_page = paginator.get_page(page) # вызывает ошибку, если страница (атрибут page) не найдена


    context = {
        'title': 'Home - каталог',
        'goods': current_page,
        'slug_url': category_slug,
    }
    return render(request, 'goods/catalog.html', context)




def product(request, product_slug):
    product  = Products.objects.get(slug=product_slug)
    context = {
        'product': product
    }
    return render(request, 'goods/product.html', context)