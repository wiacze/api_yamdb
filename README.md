# Проект API YaMDb

## Описание
Проект **YaMDb** собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. 

Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.

## Установка
1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/wiacze/api_yamdb.git
    ```

    ```
    cd api_yamdb
    ```
2. Создать и активировать виртуальное окружение:
    
    Для OS Windows:
    ```
    python -m venv venv
    ```

    ```
    source venv/Scripts/activate
    ```
    Для OS Linux/MacOS:
    ```
    python3 -m venv venv
    ```

    ```
    source venv/bin/activate
    ```

3. Обновите pip и установите зависимости:
    ```bash
    python -m pip install --upgrade pip
    ```
    ```bash
    pip install -r requirements.txt
    ```
4. Выполните миграции:
    ```bash
    python manage.py migrate
    ```
5. Запустите сервер разработки:
    ```bash
    python manage.py runserver
    ```

## Ресурсы API

Запросы к API начинаются с ```/api/v1/```

```/auth/signup/```: Создание пользователя и авторизация

```/auth/token/```: Аутентификация по токену

```/users/```: Получение списка и создание новых пользователей (администратор)

```/users/me/```: Управление собственным профилем

```/users/{username}/```: Управление пользователями по username

```/titles/```: Произведения (фильмы, книги, песни)

```/categories/```: Категории произведений

```/genres/```: Жанры произведений

```/reviews/```: Отзывы на произведения

```/comments/```: Комментарии к отзывам

## Права доступа

- **Анонимный пользователь** - Может просматривать описания произведений, читать отзывы и комментарии.
- **Аутентифицированный пользователь** - Может читать всё, публиковать отзывы, ставить оценки произведениям, комментировать отзывы, а также редактировать/удалять свои отзывы, комментарии и оценки
- **Модератор** - Те же права, что и у аутентифицированного пользователя, плюс возможность удалять и редактировать любые отзывы и комментарии
- **Администратор** - Полные права на управление всем контентом, может создавать и удалять произведения, категории и жанры, а также назначать роли пользователям

## Техническая информация:
1. Язык программирования: [`Python v.3.9.13`](https://www.python.org/downloads/release/python-3913/)
1. Библиотеки: \
            2.1. [`Django`](https://www.djangoproject.com/)(v.3.2.16)- используется для создания веб-приложений, включая API. \
            2.2. [`Django REST Framework`](https://www.django-rest-framework.org/)(v.3.12.4) - используется для создания REST API в Django. \
            2.3. [`pytest`](https://docs.pytest.org/en/stable/)(v6.2.4) - фреймворк для написания и запуска тестов. \
            2.4. [`pytest-django`](https://pytest-django.readthedocs.io/en/latest/)(v4.4.0) - плагин для pytest, который предоставляет средства для тестирования Django-приложений. \
            2.5. [`pytest-pythonpath`](https://pypi.org/project/pytest-pythonpath/)(v0.7.3) - плагин для pytest, который позволяет использовать PYTHONPATH для импорта модулей в тестах. \
            2.6. [`djangorestframework-simplejwt`](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)(v4.2.7.) - библиотека для простой реализации JWT-авторизации в DRF. \
            2.7. [`PyJWT`](https://pyjwt.readthedocs.io/en/stable/)(v2.1.0) - библиотека для работы с JSON Web Tokens (JWT). \
            2.8. [`requests`](https://requests.readthedocs.io/en/master/)(v2.26.0) - библиотека для отправки HTTP-запросов. \
            2.9. [`django-filter`](https://django-filter.readthedocs.io/en/stable/guide/install.html)(v.23.1) - библиотека для фильтрации запросов к API.
