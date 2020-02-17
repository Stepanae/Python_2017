from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import *


class RegistrationForm(UserCreationForm):
    username = CharField(min_length=5, label='Логин')
    password1 = CharField(min_length=8, widget=PasswordInput, label='Пароль')
    password2 = CharField(min_length=8, widget=PasswordInput, label='Повторите ввод')
    email = EmailField(label='Email')
    first_name = CharField(max_length=30, label='Введите имя')
    last_name = CharField(max_length=30, label='Введите фамилию')

    class Meta:
        fields = [
            'username',
            'password1',
            'password2',
            'email',
            'first_name',
            'last_name'
        ]
        model = User


class AuthorizationForm(AuthenticationForm):
    username = CharField(min_length=5, label='Логин')
    password = CharField(min_length=8, widget=PasswordInput, label='Пароль')
