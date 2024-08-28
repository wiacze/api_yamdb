"""Custom user model for YaMDb project."""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ValidationError

from reviews.constants import CODE_LENGTH, ROLE_LENGTH


class CustomUser(AbstractUser):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (MODERATOR, 'Moderator'),
        (USER, 'User')
    )
    bio = models.TextField(blank=True, verbose_name='О себе')
    role = models.CharField(
        max_length=ROLE_LENGTH,
        choices=ROLE_CHOICES,
        default=USER,
        verbose_name='Статус'
    )
    email = models.EmailField(
        'Почтовый адрес',
        unique=True
    )
    confirmation_code = models.CharField(
        'Код авторизации',
        max_length=CODE_LENGTH,
        default='',
        blank=True,
    )

    def clean(self):
        super().clean()
        if self.username == 'me':
            raise ValidationError(
                '`me` нельзя использовать в качестве имени!'
            )

    @property
    def is_admin(self):
        return self.role == 'admin' or self.is_superuser

    @property
    def is_moder(self):
        return self.role == 'moderator'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
