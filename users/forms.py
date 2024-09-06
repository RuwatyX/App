from dataclasses import fields
from django.forms import (
    CharField,
    EmailField,
    EmailInput,
    ImageField,
    FileInput,
    TextInput,
)
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
)

from users.models import User


class UserLoginForm(AuthenticationForm): # используется модель из AUTH_USER_MODEL (users.User)
    class Meta:
        fields = ["username", "password"]


class UserRegistrationForm(UserCreationForm):   
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]

    # first_name = CharField()
    # last_name = CharField()
    # username = CharField()
    # email = CharField()
    # password1 = CharField()
    # password2 = CharField()


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["image", "first_name", "last_name", "username", "email"]
    
    
    # class Meta:
    #     model = User
    #     fields = ["image", "first_name", "last_name", "username", "email"]

    # image = ImageField(
    #     widget=FileInput(attrs={"class": "form-control mt-3"}), required=False
    # )
    # first_name = CharField(
    #     widget=TextInput(
    #         attrs={"class": "form-control", "placeholder": "Введите ваше имя"}
    #     )
    # )
    # last_name = CharField(
    #     widget=TextInput(
    #         attrs={"class": "form-control", "placeholder": "Введите вашу фамилию"}
    #     )
    # )
    # username = CharField(
    #     widget=TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введите ваше имя пользователя",
    #         }
    #     )
    # )
    # email = EmailField(
    #     widget=EmailInput(
    #         attrs={"class": "form-control", "placeholder": "Введите вашу почту"}
    #     )
    # )
