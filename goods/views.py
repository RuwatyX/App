from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, get_list_or_404
from goods.models import Categories, Products


def catalog(request, category_slug):
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)

    if category_slug == 'all':
        goods = Products.objects.all()
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


    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)


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