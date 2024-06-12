# Electronics Retail Online Platform

## О проекте
Данный проект представляет собой веб-приложение с API-интерфейсом и админ-панелью для управления сетью по продаже электроники. Проект создан с использованием Django, Django REST framework и PostgreSQL.

## Требования
- Python 3.8+
- Django 3+
- Django REST framework 3.10+
- PostgreSQL 10+

## Установка
1. Склонируйте репозиторий на свой локальный компьютер.
2. Создайте виртуальное окружение и активируйте его.
3. Установите зависимости из файла `requirements.txt`:
   ```
   pip install -r requirements.txt
   ```
4. Создайте файл `.env` и добавьте в него необходимые настройки для подключения к базе данных.
Пример содержимого для файла `.env` представлен в файле `sample.env`
   ```
   # Настройки для подключения к БД

   DB_USER='username'
   DB_PASSWORD='password'
   DB_HOST='localhost'
   DB_NAME='database_name'
   DB_PORT='5432'
   ```
6. Примените миграции:
   ```
   python manage.py migrate
   ```
7. Запустите сервер разработки:
   ```
   python manage.py runserver
   ```

## Структура проекта

- `retail_platform` Содержит модели, представления, сериализаторы, разрешения, тесты для платформы электроники.
- `users` Содержит модели, представления, сериализаторы, разрешения, тесты для управления пользователями.
- `config` Основные настройки проекта и URL-адреса.

## Функциональность
- Модели: реализована иерархическая структура сети по продаже электроники на базе Django моделей.
- Админ-панель: вывод и возможность управления объектами сети (поставщики, контакты, товары).
- API: реализованы CRUD операции для поставщиков и товаров с установленными правами доступа.

## Документация API
API документирована с помощью инструмента DRF YASG. Документацию можно просмотреть через:
- Swagger UI: `/docs/`
- ReDoc: `/redoc/`

## Автор
Проект разработал **[Sergey Semyonov]**.
