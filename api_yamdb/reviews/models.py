from django.db import models


class Category(models.Model):
    """Модель категории."""
    name = models.CharField(
        verbose_name='Название группы',
        max_length=256,
    )
    slug = models.SlugField(
        verbose_name='Идентификатор группы',
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
        verbose_name='Описание произведения'
    )
    year = models.SmallIntegerField(
        verbose_name='Год выпуска'
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        related_name='titles',
        on_delete=models.CASCADE
    )
    genre = models.ManyToManyField(Genre)
