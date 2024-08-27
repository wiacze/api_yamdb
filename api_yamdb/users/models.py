"""Custom user model for YaMDb project."""

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Кастомная модель пользователя."""
    username = models.CharField(max_length=50, unique=True, verbose_name='username')
