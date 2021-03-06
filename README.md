Сервис менеджер товаров магазинов
=======

Запуск сервисов
-------

Для запуска нужен Docker и docker-compose

В корне проекта запустить команду:
```shell
docker-compose -f ./docker-compose.prod.yml up -d --build
```

После этой команды должны подняться 4 сервиса: 
- backend (django, gunicorn, nginx) Адрес: http://localhost:8080
- backend_db (postgres) Закрыт извне
- cache (memcache) Тоже закрыт
- frontend (vuejs, nginx) Адрес: http://localhost:80

Запуск тестов
-------

Чтобы запустить тесты, необходимо выполнить эту команду (после того как сервисы были запущены):
```shell
docker exec -it productmanagerproject_backend python manage.py test
```

Предварительная настройка
-------

Когда поднимается бэкенд выполняются все необходимые команды кроме одной - создания суперпользователя
Чтобы создать суперпользователя, необходимо выполнить эту команду (после того как сервисы были запущены):
```shell
docker exec -it productmanagerproject_backend python manage.py createsuperuser
```

Документация Rest сервиса
-------

После этого можно зайти в административную панель по адресу: http://localhost:8080/admin/  
А после логина под админом можно посмотреть документацию swagger: http://localhost:8080/swagger/  
Еще ReDoc сгенерировалась, но я ей не пользовался при разработке и не знаю как там она поживает: http://localhost:8080/redoc/

Остановка сервисов
-------

Для остановки сервисов необходимо выполнить эту команду:  
**WARNING!!!**
Флаг `-v` говорит, чтоб уничтожились все созданные volumes, 
поэтому если в базу вносились изменения, которые хотелось 
бы увидеть после остановки сервисов при след. запуске, то тогда этот флаг надо убрать
```shell
docker-compose -f docker-compose.prod.yml down -v
```
