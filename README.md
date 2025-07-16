# blog_api
## Описание
    Проект blog_api представляет собой API платформу для людей, ведущих свои блоги. 
    Функционал:
    Возможность регистрации, создание записей, просмотр записей других пользователей, комментирование записей и подписка на других пользователей.

     Обмен данными осуществляется через API.


## Запуск проекта
1. Клонирование репозитория
    В рабочей папке выполнить команду:
    >> git_clone https://github.com/Nikolay-Botskalev/api_final_yatube
2. Создание виртуального окружения
    >> python -m venv venv
3. Активация виартуального окружения
    >> source venv/scripts/activate
4. Установка зависимостей
    >> pip install -r requirements.txt
5. Выполнение миграций
    Перейти в директорию с файлом manage.py:
    >> cd blog_api
    Выполнить команду:
    >> python manage.py migrate
6. Запуск сервера
    >> python manage.py runserver
Готово

## Примеры некоторых запросов.
1. Запрос списка публикаций (GET-запрос)
    >> http://127.0.0.1:8000/api/v1/posts/
    Ответ:
    [
        {
            "id": 1,
            "author": "regular_user",
            "text": "Пост зарегистрированного пользователя 1.",
            "pub_date": "2024-07-19T19:06:49.634740Z",
            "image": null,
            "group": null
        },
        {
            "id": 2,
            "author": "user2",
            "text": "Пост зарегистрированного пользователя 2.",
            "pub_date": "2024-07-19T19:06:49.634740Z",
            "image": null,
            "group": 1
        }
    ]
2. Создание публикации (POST-запрос)
    >> http://127.0.0.1:8000/api/v1/posts/
    Пример запроса:
    {
    "id": 2,
    "author": "user2",
    "text": "Пост зарегистрированного пользователя 2.",
    "pub_date": "2024-07-19T19:06:49.634740Z",
    "image": null,
    "group": 1
    }
3. Запрос комментариев к посту (GET-запрос)
    >> http://127.0.0.1:8000/api/v1/posts/14/comments/
    Ответ:
    {
    "id": 1,
    "author": "regular_user",
    "text": "Тестовый комментарий",
    "created": "2024-07-19T19:06:50.328206Z",
    "post": 14
    }
4. Добавление комментария (POST-запрос)
    >> http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
    Пример запроса:
    {
    "text": "Текст комментария"
    }
5. Запрос информации о группе
    >> http://127.0.0.1:8000/api/v1/groups/1/
    Ответ:
    {
    "id": 1,
    "title": "TestGroup",
    "slug": "test-group",
    "description": "Описание группы."
    }
6. Запрос информации о подписках
    >> http://127.0.0.1:8000/api/v1/follow/
    Ответ:
    [
        {
            "user": "regular_user",
            "following": "root"
        },
        {
            "user": "regular_user",
            "following": "second_user"
        }
    ]

## Заполенение .env файла.

Пример заполненного файла .env:
```
SECRET = <Ваш SECRET_KEY>
DEBUG = <True/False>
```

## [Автор](https://github.com/Nikolay-Botskalev)
