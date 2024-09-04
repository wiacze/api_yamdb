# API YaMDb

## Описание
Проект **YaMDb** собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. 

Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.

## Задача API:

### API для сервиса “YaMDb” призвано обеспечить программно-ориентированное взаимодействие с сервисом для:

1. <b>Внешних приложений</b>: Позволяет другим приложениям и сервисам получать доступ к данным сервиса “YaMDb” и управлять ими, интегрируя функциональность сервиса в свои собственные решения. Например: \
1.1. <b>Новостные агрегаторы</b>: Могут подключаться к API для получения информации о новых произведениях, отзывах и комментариях, чтобы показывать их в своих лентах.\
1.2. <b>Инструменты аналитики</b>: Могут получать данные (например, количество отзывов на произведения, популярность произведений по количеству отзывов и рейтингу, средняя оценка произведений), чтобы создавать отчеты. \
1.3. <b>Боты</b>: Могут взаимодействовать с API для автоматизации задач, таких как модерация отзывов, комментариев и т.п.
1. <b>Внутренних систем</b>: Упрощает обмен данными между различными компонентами сервиса “YaMDb”, позволяя разработчикам легко интегрировать новые функции и оптимизировать работу сервиса.

## Польза API:

1. <b>Улучшение взаимодействия</b>: Предоставляет разработчикам удобный и структурированный способ взаимодействия с сервисом, вместо ручного парсинга HTML-страниц.
2. <b>Расширение возможностей</b>: Открывает новые возможности для интеграции с другими сервисами и приложениями, расширяя функциональность сервиса ““YaMDb””.
3. <b>Упрощение разработки</b>: Обеспечивает более быструю и эффективную разработку новых функций и инструментов для сервиса, так как разработчики могут работать с API вместо непосредственного доступа к базе данных.
4. <b>Повышение гибкости</b>: Позволяет легко добавлять и изменять функциональность API без необходимости изменения фронтенд-части сервиса.
5. <b>Создание экосистемы</b>: API может стать основой для создания экосистемы внешних приложений и инструментов, которые обогащают функциональность сервиса “YaMDb”.

## Структура проекта
<pre>└── api_yamdb
     ├── api_yamdb
     │  ├── api
     │  ├── api_yamdb
     │  ├── reviews
     │  ├── static
     │  ├── templates
     │  ├── users
     │  ├── db.sqlite3
     │  └── manage.py
     ├── postman_collection
     ├── tests
     ├── .gitignore
     ├── pytest.ini
     ├── README.md
     ├── requirements.txt 
     └── setup.cfg</pre>


## Установка
### Клонирование репозитория
1. Выполните в [Git Bash](https://gitforwindows.org) команду:\
`
git clone https://github.com/wiacze/api_yamdb.git
`
### Установка и активация виртуального окружения
1. Перейдите в директорию проекта. \
   `C:/.../ваш_проект`
2. Если вы уже создавали для проекта виртуальное окружение, удалите его:\
   `rm -r venv`
3. Создайте и активируйте новое виртуальное окружение:
   ```
   # Команды для Windows:

   python -m venv .venv
   source .venv/Scripts/activate

   # Команды для Linux и macOS:

   python3 -m venv .venv
   source .venv/bin/activate
   ```
### Установка и обновление пакетного менеджера(pip)
1. Проверьте установлен ли у вас пакетный менеджер:\
   `pip --version`

2. Если он не установлен выполните следующую команду: \
   `python -m pip install --upgrade pip `
### Установка зависимостей
1. Для установки зависимостей выполните команду: \
`pip install -r requirements.txt`

### Импорт пресетов для бд
1. Перейдите в корневую директорию \
    `cd api_yamdb`

2. Выполните миграции \
   `python manage.py migrate`

3. Выполните команду для импорта \
    `python manage.py csv_import`

### Запуск локального сервера
1. Из корневой директории выполните команду \
    `python manage.py runserver`

## Примеры запросов

### Регистрация нового пользователя
#### 1. Получение кода подтверждения
```
POST http://127.0.0.1:8000/api/v1/auth/signup/
```
<details>
  <summary>Request body</summary>
    <pre>{
    "username": "TestUser1",
    "email": "testuser@mail.ru"
}</pre>
</details>

#### На почту пользователя отправлено сообщение с кодом подтверждения
<details>
  <summary>Email</summary>
    <pre>Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 8bit
Subject: =?utf-8?b?0JrQvtC0INC/0L7QtNGC0LLQtdGA0LbQtNC10L3QuNGP?=
From: YaMDB@mail.com
To: testuser@mail.ru
Date: Wed, 04 Sep 2024 14:30:49 -0000
Message-ID: <172546024996.20956.17031334500321012374@DESKTOP-AH1FLS4>

Ваш код подтверждения: ccugvd-3e322b52289f97a8989aa16548615eb8
-------------------------------------------------------------------------------</pre>
</details>

#### 2. Получить токен
```
POST http://127.0.0.1:8000/api/v1/auth/token/
```
<details>
  <summary>Request body</summary>
    <pre>{
    "username": "TestUser1",
    "confirmation_code": "ccugvd-3e322b52289f97a8989aa16548615eb8"
}</pre>
</details>

<details>
  <summary>Response</summary>
    <pre>{
    "token": "eyJ0eXGYmYzNG0.I9EXuifwaVqo6ZpJ3Lc1Dj9QwYHyDiKnr8VzvBYNZuI"
}   </pre>
</details>

--- 

### Получение списка категорий
```
GET http://127.0.0.1:8000/api/v1/categories/
```

<details>
  <summary>Response</summary>
    <pre>{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "name": "Книга",
            "slug": "book"
        },
        {
            "name": "Фильм",
            "slug": "movie"
        },
        {
            "name": "Музыка",
            "slug": "music"
        }
    ]
}   </pre>
</details>

---

### Получение списка жанров
```
GET http://127.0.0.1:8000/api/v1/genres/
```
<details>
  <summary>Response</summary>
    <pre>{
    "count": 15,
    "next": "http://127.0.0.1:8000/api/v1/genres/?page=2",
    "previous": null,
    "results": [
        {
            "name": "Баллада",
            "slug": "ballad"
        },
        {
            "name": "Шансон",
            "slug": "chanson"
        },
        {
            "name": "Классика",
            "slug": "classical"
        },
        {
            "name": "Комедия",
            "slug": "comedy"
        },
        {
            "name": "Детектив",
            "slug": "detective"
        }
    ]
}   </pre>
</details>

--- 

### Получение списка произведений
```
GET http://127.0.0.1:8000/api/v1/titles/
```

<details>
  <summary>Response</summary>
    <pre>{
    "count": 32,
    "next": "http://127.0.0.1:8000/api/v1/titles/?page=2",
    "previous": null,
    "results": [
        {
            "id": 3,
            "name": "12 разгневанных мужчин",
            "year": 1957,
            "rating": 8,
            "description": "",
            "genre": [
                {
                    "name": "Драма",
                    "slug": "drama"
                }
            ],
            "category": {
                "name": "Фильм",
                "slug": "movie"
            }
        },
        {
            "id": 30,
            "name": "Deep Purple — Smoke on the Water",
            "year": 1971,
            "rating": 10,
            "description": "",
            "genre": [
                {
                    "name": "Рок",
                    "slug": "rock"
                }
            ],
            "category": {
                "name": "Музыка",
                "slug": "music"
            }
        },
        {
            "id": 29,
            "name": "Elvis Presley - Blue Suede Shoes",
            "year": 1955,
            "rating": 10,
            "description": "",
            "genre": [
                {
                    "name": "Rock-n-roll",
                    "slug": "rock-n-roll"
                }
            ],
            "category": {
                "name": "Музыка",
                "slug": "music"
            }
        },
        {
            "id": 19,
            "name": "Generation П",
            "year": 2011,
            "rating": 9,
            "description": "",
            "genre": [
                {
                    "name": "Драма",
                    "slug": "drama"
                }
            ],
            "category": {
                "name": "Фильм",
                "slug": "movie"
            }
        },
        {
            "id": 24,
            "name": "Generation П",
            "year": 1999,
            "rating": 6,
            "description": "",
            "genre": [
                {
                    "name": "Роман",
                    "slug": "roman"
                }
            ],
            "category": {
                "name": "Книга",
                "slug": "book"
            }
        }
    ]
}   </pre>
</details>

--- 

### Получение списка отзывов к произведению
```
GET http://127.0.0.1:8000/api/v1/titles/3/reviews/
```

<details>
  <summary>Response</summary>
    <pre>{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 16,
            "text": "Сходила в кино, решила написать: драйв и огонь, но иногда какой-то бред на экране. В середине фильма просто отличные диалоги! Пусть будет 7",
            "author": "bingobongo",
            "score": 7,
            "pub_date": "2024-09-03T23:32:39.332214+03:00"
        },
        {
            "id": 17,
            "text": "Смотрел, не отрываясь, хочу описать свои впечатления. По моему мнению, сценарий подкачал, зато подбор актёров - супер. Начало немного затянуто. Оператору - Оскара! Всё остальное - не очень. Фильм тянет на 8 из 10",
            "author": "capt_obvious",
            "score": 8,
            "pub_date": "2024-09-03T23:32:39.337200+03:00"
        }
    ]
}   </pre>
</details>

--- 

### Создание отзыва к произведению
```
POST http://127.0.0.1:8000/api/v1/titles/3/reviews/
```
<details>
  <summary>Request body</summary>
    <pre>{
    "text": "Test review",
    "score": 10
}</pre>
</details>

<details>
  <summary>Response</summary>
    <pre>{
    "id": 76,
    "text": "Test review",
    "author": "TestUser1",
    "score": 10,
    "pub_date": "2024-09-04T17:47:04.788641+03:00"
}   </pre>
</details>

--- 

### Изменение отзыва
```
PATCH http://127.0.0.1:8000/api/v1/titles/3/reviews/76/
```
<details>
  <summary>Request body</summary>
    <pre>{
    "text": "new test review",
    "score": 8
}</pre>
</details>

<details>
  <summary>Response</summary>
    <pre>{
    "id": 76,
    "text": "new test review",
    "author": "TestUser1",
    "score": 8,
    "pub_date": "2024-09-04T17:47:04.788641+03:00"
}   </pre>
</details>

--- 

### Удаление отзыва
```
DELETE http://127.0.0.1:8000/api/v1/titles/3/reviews/76/
```

<details>
  <summary>Response</summary>
    <pre>204 - No Content</pre>
</details>


--- 

### Получение списка комментариев к отзыву
```
GET http://127.0.0.1:8000/api/v1/titles/3/reviews/77/comments/
```
<details>
  <summary>Response</summary>
    <pre>{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 4,
            "review": "Test review",
            "author": "TestUser1",
            "text": "Test comment 1",
            "pub_date": "2024-09-04T18:10:20.667795+03:00"
        },
        {
            "id": 5,
            "review": "Test review",
            "author": "TestUser1",
            "text": "Test comment 2",
            "pub_date": "2024-09-04T18:10:48.248829+03:00"
        },
        {
            "id": 6,
            "review": "Test review",
            "author": "TestUser1",
            "text": "Test comment 3",
            "pub_date": "2024-09-04T18:10:50.985962+03:00"
        }
    ]
}</pre>
</details>

### Создание комментария к отзыву
```
POST http://127.0.0.1:8000/api/v1/titles/3/reviews/77/comments/
```
<details>
  <summary>Request body</summary>
    <pre>{
    "text": "Test comment 3",
}</pre>
</details>

<details>
  <summary>Response</summary>
    <pre>{
    "id": 6,
    "review": "Test review",
    "author": "TestUser1",
    "text": "Test comment 3",
    "pub_date": "2024-09-04T18:10:50.985962+03:00"
}</pre>
</details>

## Ресурсы API

Запросы к API начинаются с ```/api/v1/```

```/auth/signup/```: Создание пользователя и авторизация

```/auth/token/```: Получение токена

```/users/```: Получение списка и создание новых пользователей (администратор)

```/users/me/```: Получение и управление данными своей учетной записи

```/users/{username}/```: Получение и управление пользователями по username (администратор)

```/categories/```: Категории произведений

```/genres/```: Жанры произведений

```/titles/```: Произведения (фильмы, книги, песни)

```/titles/{title_id}/```: Получение информации о произведении

```/{title_id}/reviews/```: Отзывы на произведения

```/reviews/{review_id}/```: Получение отзыва по id

```/{review_id}/comments/```: Комментарии к отзывам

```/comments/{comment_id}/```: Получение комментария по id

#### Полная документация будет доступна по адресу [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

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

#### Над проектом работали:
[`Ян Языков`](https://github.com/wiacze)
[`Камиль Высоцкий`](https://github.com/KamilVysotskij)
[`Антон Савченко`](https://github.com/Anthonyz1337)
