from django.contrib import admin
from goods.models import Categories, Products
# Register your models here.

# admin.site.register(Categories) # Регистрация таблицы в админ панели
# admin.site.register(Products) # Регистрация таблицы в админ панели

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
      