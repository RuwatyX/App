from django.urls import path
from goods import views


app_name = 'goods'

urlpatterns = [
    path('', views.catalog, name='index'), 
    # name необходимо указать чтобы затем использовать в шаблонах
    path('product/', views.product, name='product'),
]