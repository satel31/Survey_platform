# Проект "Платформа опросов"

## Краткое описание

Приложение, в которой зарегистрированный пользователь может размещать опросы (с вопросами, вариантами ответа), проходить
опросы, делиться опросами, оценивать их.
Проект выполнен на Windows.
Создан с использованием Python и Django REST framework. Авторизация настроена с помощью библиотеки drf-social-oauth2 (
через Google), настроен вывод документации через Swagger. Управление всеми сущностями реализовано также через Django
Admin. В качестве базы данных используется PostgreSQL.
Для проверки функциональности прописаны тесты. Покрытие составляет 97% (проверялось с помощью библиотеки coverage).
Для проверки на соответствие PEP8 использовалась библиотека flake8.

## Инструкция по запуску

1. Создайте файл .env по образцу в файле .env.sample.
2. Установите зависимости проекта, указанные в файле pyproject.toml.
   ```bash
   poetry install
   ```
3. Выполните миграции
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Запустите сервер:
   ```bash
   python manage.py runserver
   ```
5. При необходимости загрузите тестовые данные с помощью фикстур или же внесите свои собственные данные.
   ```bash
   python manage.py loaddata learning_data.json
   python manage.py loaddata user_data.json
   ```
6. Получить токен для работы с приложением можно в OAuth 2.0 Playground (https://developers.google.com/oauthplayground/)
    * Для этого выберите Google OAuth2 API v2 в списке (email и profile), сформировать код и преобразовать его в токен (
      Exchange authorization code for tokens).
    * Далее передайте токен в POST запросе к http://localhost:8000/auth/convert-token:
    ```bash
   {
        "client_id": "client_id",
        "grant_type": "convert_token",
	    "client_secret": "client_secret",
	    "backend": "google-oauth2",
	    "token": <Токен из предыдущего шага>,
   }
   ```
    * Полученный Access token можно использовать для работы с приложением.

## Технологии в проекте (стек)

* Python 3.11
* Django
* DRF
* PostgreSQL
* OAuth2.0
* Swagger
* Unittest
