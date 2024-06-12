from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

from users.managers import UserManager

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """ Модель пользователя. """

    groups = models.ManyToManyField(Group, related_name='custom_users_group')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')

    username = None

    email = models.EmailField(
        unique=True,
        verbose_name='E-mail'
    )
    code = models.CharField(
        default='XXX',
        max_length=3,
        verbose_name='Код телефона'
    )
    phone = models.CharField(
        default='XXXXXXX',
        max_length=7,
        verbose_name='Номер телефона'
    )
    city = models.CharField(
        max_length=20,
        **NULLABLE,
        verbose_name='Город'
    )
    avatar = models.ImageField(
        upload_to='images/users/',
        **NULLABLE,
        verbose_name='Аватарка'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    @property
    def full_number(self):
        """ Возвращает полный номер телефона пользователя. """
        return f"+ 7 ({self.code}) {self.phone}"

    def __str__(self):
        """ Возвращает строковое представление о модели пользователя. """
        if self.first_name:
            return f'{self.first_name}'
        return f'{self.email}'

    class Meta:
        """ Метаданные для модели пользователя. """
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
