from django.db import models
from users.managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=20,
        verbose_name="Имя"
    )
    first_name = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="Фамилия"
    )
    password = models.CharField(
        max_length=20,
        verbose_name="Пароль"
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Почтовый адрес"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Активный"
    )
    is_staff = models.BooleanField(
        default=True,
        verbose_name="Сотрудник"
    )

    objects = CustomUserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "password"]

    def __str__(self):
        return f"{self.username}"