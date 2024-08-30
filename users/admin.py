from django.contrib import admin
from django.urls import include
from carts.admin import CartTabAdmin
from users.models import User
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email"]
    search_fields = ["first_name", "last_name", "username", "email"]
    inlines = [CartTabAdmin]