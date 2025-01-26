
## Структура репозитория
1. `tests` = <api/tests.py>
2. `code` = < api >
3. `docker` = <Название `Dockerfile` и `docker-compose.yml`>
4. `migrations` = <api/migrations>

## Инструкции по локальному запуску
1. Клонировать репозиторий:
```git clone https://github.com/nurlan5t/medapp.git```
```cd medapp```

2. Установить зависимости:
```pip install -r requirements.txt```

3. Применить миграции:
```python manage.py migrate```

4. Запустить сервер:
```python manage.py runserver```

## Запуск в Docker
1. Собрать и запустить контейнеры:
```docker-compose up --build```

2. Доступ к серверу будет по адресу
```http://localhost:8000```

## Тестирование
```python manage.py test```

## Примеры запросов
Login:
POST ```/api/login/```

Пример тела запроса:
```
{
  "username": "doctor1",
  "password": "password123"
}
```
Patients (для докторов):
GET ```/api/patients/```

Пример заголовка:
```Authorization: Bearer <your_jwt_token>```
