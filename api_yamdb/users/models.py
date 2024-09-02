"""Custom user model for YaMDb project."""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

from .utils import Role


class CustomUser(AbstractUser):
    """Кастомная модель пользователя."""

    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=150,
        unique=True,
        validators=[RegexValidator(r'^[\w.@+-]+$'),],
    )
    email = models.EmailField(
        verbose_name='Email',
        max_length=254,
        unique=True
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=150,
        blank=True
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=150,
        blank=True
    )
    bio = models.TextField(
        verbose_name='Биография',
        blank=True
    )
    role = models.CharField(
        verbose_name='Роль',
        max_length=Role.max_length(),
        choices=Role.selection(),
        default=Role.user.name
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)

    def __str__(self):
        return self.username

    @property
    def is_moder(self):
        return self.role == Role.moderator.name

    @property
    def is_admin(self):
        return self.role == Role.admin.name

    def save(self, *args, **kwargs):
        """
        Если в чекбоксе отмечен is_superuser, присваивает роль админ.
        Не меняет роли у уже созданных пользователей.
        """
        if self.is_superuser and not self.pk:
            self.role = Role.admin.name
        super().save(*args, **kwargs)
