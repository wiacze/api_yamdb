from django.core.exceptions import ValidationError
from django.db import models
from datetime import datetime


class Category(models.Model):
    """Модель категории."""
    name = models.CharField(
        verbose_name='Название категории',
        max_length=256,
    )
    slug = models.SlugField(
        verbose_name='Идентификатор категории',
        help_text=('Идентификатор страницы для URL; разрешены символы '
                   'латиницы, цифры, дефис и подчёркивание.'),
        unique=True
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Модель жанра."""
    name = models.CharField(
        verbose_name='Название жанра',
        max_length=256,
    )
    slug = models.SlugField(
        verbose_name='Идентификатор жанра',
        help_text=('Идентификатор страницы для URL; разрешены символы '
                   'латиницы, цифры, дефис и подчёркивание.'),
        unique=True
    )

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Title(models.Model):
    """Модель произведения"""
    name = models.CharField(
        verbose_name='Название произведения',
        max_length=256
    )
    description = models.TextField(
        verbose_name='Описание произведения',
        blank=True
    )
    year = models.SmallIntegerField(
        verbose_name='Год выпуска'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория',
        related_name='titles',
    )
    genre = models.ManyToManyField(
        Genre,
    )

    class Meta:
        verbose_name = 'произведение',
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name

    def clean(self):
        if self.year > datetime.now().year:
            raise ValidationError(
                "Год выпуска не может быть больше текущего года."
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
