from django.urls import path
from goods import views


app_name = 'catalog'

urlpatterns = [
    path('<slug:category_slug>/', views.catalog, name='index'), 
    path('<slug:category_slug>/<int:page>/', views.catalog, name='index'), 

    # name необходимо указать чтобы затем использовать в шаблонах
    path('product/<slug:product_slug>/', views.product, name='product'),
]
# category_slug или product_slug - имя параметра, его нужно перенести в контроллер
