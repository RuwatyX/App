from django.contrib import admin
from orders.models import Order, OrderItem
from users.models import User


class OrderItemTabularAdmin(admin.TabularInline):
    model = OrderItem
    fields = ["product", "name", "price", "quantity"]
    search_fields = ["product", "name"]
    extra = 0




class OrderTabularAdmin(admin.TabularInline):
    model = Order
    fields = (
        "requires_delivery",
        "status",
        "payment_on_get",
        "is_paid",
        "created_timestamp"
    )

    search_fields = ("requires_delivery", "payment_on_get", "is_paid", "created_timestamp")
    readonly_fields = ("created_timestamp",)
    extra = 0

    



@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin): # Отдельный заказанный товар
    list_display = ["order", "product", "name", "price", "quantity", ]
    search_fields = ["product", "name", "price"]


    

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin): # Информация об отдельном заказанном товаре
    list_display = [
        "id",
        "user",
        "requires_delivery",
        "status",
        "payment_on_get",
        "is_paid",
        "created_timestamp"
    ]

    search_fields = [
        "id",
        "is_paid",
        "created_timestamp"
    ]

    readonly_fields = ["created_timestamp", ]

    list_filter = [
        "id",
        "user",
        "requires_delivery",
        "status",
        "payment_on_get",
        "is_paid",
        "created_timestamp"
    ]

    inlines = [OrderItemTabularAdmin]




