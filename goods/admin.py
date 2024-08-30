from django.contrib import admin
from goods.models import Categories, Products
# Register your models here.

# admin.site.register(Categories) # Регистрация таблицы в админ панели
# admin.site.register(Products) # Регистрация таблицы в админ панели

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ["name"]

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ["name", "quantity", "price", "discount"] # какие столбцы будут отображаться
    list_editable = ["discount"] # какие столцы можно изменять прямо в админ панели
    search_fields = ["name", "description"] # добавление поиска + поля по которым будет осуществляться поиск
    list_filter = ["discount", "quantity", "category"]
    fields = [ # в каком порядке мы хотим чтобы отображались документы
        "name",
        "category",
        "slug",
        "description",
        "image",
        ("price", "discount"),
        "quantity"
    ]