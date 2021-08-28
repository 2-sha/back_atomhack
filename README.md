# Как с этим жить

### Начальная настройка
По умолчанию стоит БД `atomhack` с пользователем `admin` и паролем `admin`. В `application/settings.py` можно поменять. 

Можно войти в админку: `http://127.0.0.1:8000/admin/`

### Команды
```bash
# Применение миграций
python ./manage.py migrate
# Создание пользователя админа
python ./manage.py createsuperuser
# Запуск сервера
python ./manage.py runserver
```

### Моковые данные
```bash
# Сгенерировать 100 пользователей
python ./manage.py generate_staff -n 100
```
