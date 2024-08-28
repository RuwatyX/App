from webbrowser import get
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from carts.models import Cart
from carts.utils import get_user_carts
from goods.models import Products
from django.http import JsonResponse


# product_slug не нужен, будет использоваться добавление по id,
# в jquery-ajax.js направляется POST запрос на указанный в шаблоне href url (на этот)
def cart_add(request):
    product_id = request.POST.get(
        "product_id"
    )  # jquery направляет POST запрос с данным ключем
    product = Products.objects.get(id=product_id)
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()

        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)

    user_cart = get_user_carts(request)

    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": user_cart}, request=request
    )
    # рендер в строку часть какой-либо разметки,
    # request нужен для нормального рендеринга шаблона, словарь (context) нужен для передачи
    # этого ключа шаблону для перебора всех товаров из корзины,
    # чтобы они могли нормально показываться пользователю

    responce_data = {
        "message": "Товар добавлен в корзину",  # используется в файле jquery-ajax.js для вывода сообщения от из переменной successMessage
        "cart_items_html": cart_items_html,  # передаем для перерисовки новое содержимое разметки, то есть обновленный шаблон корзины
    }

    return JsonResponse(responce_data)  # должен быть словарь т.к. json
    # return redirect(request.META["HTTP_REFERER"]) # с какого адреса пришел туда обратно и направляем


def cart_change(request):
    cart_id = request.POST.get("cart_id")
    quantity = request.POST.get("quantity")

    cart = Cart.objects.get(id=cart_id)
    cart.quantity = quantity
    cart.save()
    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": user_cart}, request=request
    )

    responce_data = {
        "message": "Количество изменено",
        "quantity": quantity,
        "cart_items_html": cart_items_html,
    }

    return JsonResponse(responce_data)


def cart_remove(request):
    cart_id = request.POST.get(
        "cart_id"
    )  # из POST запроса от jquery получаем id корзины
    cart = Cart.objects.get(id=cart_id)  # получаем конкретный объект корзины по id
    quantity = cart.quantity  # количество таких же товаров в корзине
    cart.delete()  # удаление корзины

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": user_cart}, request=request
    )
    # переменная, которая содержит строку, результат сформированного шаблона

    responce_data = {
        "message": "Товар удален",
        "cart_items_html": cart_items_html,
        "quantity_deleted": quantity,
    }

    return JsonResponse(responce_data)
