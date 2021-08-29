# Как с этим жить

## Распределитель задач
Это 2 файла: 
 - `NLP.ipynb` - выделение тегов из текста
 - `Router.ipynb` - распределение задач

Они берут данные из DjangoORM

## Бэкенд
По умолчанию стоит СУБД `PostresSQL`, БД `atomhack` с пользователем `admin` и паролем `admin`. В `application/settings.py` можно поменять. 

Можно войти в админку: `http://127.0.0.1:8000/admin/`

#### Команды
```bash
# Применение миграций
python ./manage.py migrate
# Создание пользователя админа
python ./manage.py createsuperuser
# Запуск сервера
python ./manage.py runserver
```

#### Моковые данные
```bash
# Сгенерировать 300 пользователей и равномерно распределить их по департаментам
python ./manage.py generate_staff -n 300 --asign
# Сгенерировать 50 тегов для зажач
python ./manage.py generate_tags -n 50
# Сгенерировать 1200 задач, проставить им теги и равномерно распределить по сотрудникам
python ./manage.py generate_staff -n 1200 --tags --assign
```
