from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, redirect
from carts.models import Cart
from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem
from django.forms import ValidationError


# Create your views here.
def create_order(request):
    if request.method == "POST":
        form = CreateOrderForm(
            data=request.POST
        )  # Заполняем форму данными из POST запроса
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user  # переменной присваиваем объект пользователя
                    cart_items = Cart.objects.filter(
                        user=user
                    )  # берем все товары (Cart) из корзины пользователя user
                    if cart_items.exists():  # если хотя бы один товар существует
                        # создаем заказ
                        order = Order.objects.create(  # take from the form validated data | формируем информацию о заказе
                            user=user,
                            phone_number=form.cleaned_data["phone_number"],
                            requires_delivery=form.cleaned_data["requires_delivery"],
                            delivery_address=form.cleaned_data["delivery_address"],
                            payment_on_get=form.cleaned_data["payment_on_get"],
                        )

                        for (
                            cart_item
                        ) in (
                            cart_items
                        ):  # итерируемся по товарам пользователя (QuerySet из объектов Cart)
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.product.sell_price()
                            quantity = cart_item.quantity

                            if (
                                product.quantity < quantity
                            ):  # если кол-во заказанных товаров меньше чем кол-во в магазине этих товаров
                                raise ValidationError(
                                    f"Недостаточное количество товара {name} на складе. \nВ наличии - {product.quantity}"
                                )

                            OrderItem.objects.create(  # создаем на каждый продукт cart_item OrderItem, то есть заказанный товар
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )

                            product.quantity -= (
                                quantity  # общее кол-во товаров минус заказанное
                            )
                            product.save()  # сохраняем в базе данных изменения для продукта

                        cart_items.delete()
                        messages.success(request, "Заказ оформлен!")
                        return redirect("user:profile")

            except ValidationError as e:
                messages.warning(request, str(e))
                return redirect("cart:order")
    else:
        initial = {
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
        }

        form = CreateOrderForm(
            initial=initial
        )  # инициализируем форму при GeT запросе с default значениями

    context = {"title": "Home - Оформление заказа", "form": form}

    return render(request, "orders/create_order.html", context=context)
