from atexit import register
from django.contrib import admin

from carts.models import Cart

class CartTabAdmin(admin.TabularInline): # Нужен для того, чтобы у пользователя отображалась корзина со всеми товарами
    model = Cart # что нужно добавить к пользователю
    fields = ["product", "quantity", "created_timestamp"] # какие поля отображать
    search_fields = ["product", "quantity", "created_timestamp"] # по каким полям позволять поиск
    readonly_fields = ["created_timestamp"] # какие поля нельзя изменять
    extra = 1 # добавление свободных полей


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["user_display", "product_display", "quantity", "created_timestamp"]
    list_filter = ["created_timestamp", "user", "product__name"]


    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return "Анонимный пользователь"
    
    def product_display(self, obj):
        return str(obj.product.name)
        

