# API_yamdb

## Описание
Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. 
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.

## Установка
1. Клонируйте репозиторий:
    ```bash
    git clone <url>
    ```
2. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
3. Выполните миграции:
    ```bash
    python manage.py migrate
    ```
4. Запустите сервер разработки:
    ```bash
    python manage.py runserver
    ```

## Ресурсы API
```/auth/: Аутентификация```

```/users/: Управление пользователями```

```/titles/: Произведения (фильмы, книги, песни)```

```/categories/: Категории произведений```

```/genres/: Жанры произведений```

```/reviews/: Отзывы на произведения```

```/comments/: Комментарии к отзывам```
