from re import T
from django.db import models

from goods.models import Products
from users.models import User

class CartQuerySet(models.QuerySet):

    def total_price(self):
        return sum(cart.products_price() for cart in self)
    # Помимо метода total_price у объекта CartQuerySet есть все методы QuerySet 
    # от которого он наследуется. self в данном случае является ссылкой на QuerySet (CartQuerySet)
    # потому что мы связали этот класс с Cart при помощи as_manager()

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0

class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь') # User - родительская таблица, при удалении пользователя User удалятся и его корзины, 
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Товар')  # каждый товар - отдельная строка таблицы
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    session_key = models.CharField(max_length=32, null=True, blank=True) # если пользователь не авторизирован, то будет использоваться это поле
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table = 'cart' # название таблицы в бд
        verbose_name = 'Корзину' # админ панель
        verbose_name_plural = 'Корзины' # admin panel

    objects = CartQuerySet().as_manager() # переопределение менеджера объектов

    def products_price(self): # self - Cart object
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self) -> str: # Для того, чтобы в админ панеле было удобно смотреть
        return f"Корзина Пользователя: {self.user.username if self.user else "Anonymous"} | Товар: {self.product.name} | Количество: {self.quantity}"
