from re import T
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser): # Наследование от автоматически сгенерированного Django класса auth_user
    image = models.ImageField(upload_to="users_images", blank=True, null=True, verbose_name='Аватар')
    # Происходит расширенние функционала родительского класса, путем добавления атрибута
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'user' # from auth_user to user
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return self.username