# Запуск проекта

- Зайдите в дерикторию __project__
---
- Cкопируйте команду и введите его в терминале.
```
docker-compose -f docker-compose.base.yml up --build
```
- Чтобы создать Админа нужно зайти в запущенный контейнер по команде
```
docker exec -it web bash
```
и ввести ``python manage.py createsuperuser``      

Так же есть команды для создания тестовых данных   

для _**категории**_ ``python manage.py fake_category int``                  
и для _**продуктов**_ ``python manage.py fake_food int``                
где int это число создаваемых обьектов в базе

