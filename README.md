# Cargo (REST API - тестовое задание)

Сервис поиска ближайших машин для перевозки грузов


## Технологии:

[![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/) [![Django](https://img.shields.io/badge/-Django-092E20?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/) [![Django Rest Framework](https://img.shields.io/badge/-Django_Rest_Framework-092E20?style=flat)](https://www.django-rest-framework.org/)
[![Celery](https://img.shields.io/badge/-Celery-37814A?style=flat&logo=celery&logoColor=white)](http://www.celeryproject.org/)
[![Redis](https://img.shields.io/badge/-Redis-DC382D?style=flat&logo=redis&logoColor=white)](https://redis.io/)
[![API](https://img.shields.io/badge/-API-4CAF50?style=flat)](https://en.wikipedia.org/wiki/Application_programming_interface)
[![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)

## Описание:

В проекте представлены следующие модели:
- Груз:
    - локация pick-up;
    - локация delivery;
    - вес (1-1000);
    - описание.
- Машина:
    - уникальный номер (цифра от 1000 до 9999 + случайная заглавная буква английского алфавита в конце, пример: "1234A", "2534B", "9999Z")
    - текущая локация;
    - грузоподъемность (1-1000).
- Локация:
    - город;
    - штат;
    - почтовый индекс (zip);
    - широта;
    - долгота.

Сервис поддерживает следующие базовые функции:
- Создание нового груза (характеристики локаций pick-up, delivery определяются по введенному zip-коду);
- Получение списка грузов (локации pick-up, delivery, количество ближайших машин до груза ( =< 450 миль));
- Получение информации о конкретном грузе по ID (локации pick-up, delivery, вес, описание, список номеров ВСЕХ машин с расстоянием до выбранного груза);
- Редактирование машины по ID (локация (определяется по введенному zip-коду));
- Редактирование груза по ID (вес, описание);
- Удаление груза по ID.
- Фильтр списка грузов (вес, мили ближайших машин до грузов);
- Автоматическое обновление локаций всех машин раз в 3 минуты (локация меняется на другую случайную).

Дополнительно:
- Загрузка локаций происходит при установке приложения.
- Также при установке приложения в БД создается 20 машин

## Эндпоинты:
### Груз:
- Создание нового груза - POST ```/api/cargo/create/```
  - Параметры:
    - zip_pickup - zip-код начальной локации
    - zip_delivery - zip-код локации доставки
    - weight - вес груза
    - description - описание груза
- Получение списка грузов - GET ```/api/cargoes/```
  - Параметры:
    - location_pickup - характеристики начальной локации
    - location_delivery - характеристики локации доставки
    - weight - вес груза
    - description - описание груза
    - nearest_cars - количество ближайших машин
- Получение информации о конкретном грузе - GET ```/api/cargo/{ID}```
  - Параметры:
    - location_pickup - характеристики начальной локации
    - location_delivery - характеристики локации доставки
    - weight - вес груза
    - description - описание груза
    - cars - список всех машин с расстоянием до груза
- Редактирование груза по ID - PATCH ```/api/cargo/update/{ID}```
  - Параметры:
    - weight - вес груза
    - description - описание груза
- Удаление груза по ID - PATCH ```/api/cargo/delete/{ID}```

### Машина:
- Редактирование машины по ID - PATCH ```/api/car/update/{ID}```
  - Параметры:
    - zip_code - изменение текущей локации по zip-коду локации

## Установка:

- Для начала работы с проектом клонируйте репозиторий:
    - ```git clone https://github.com/NickolayBabulich/cargo_api.git```
- Произвести установку Docker (https://docs.docker.com/get-docker/)
- Перейдите в корневую директорию проекта
- Запустить проект командой ```docker compose up```
- Сервис будет доступен по адресу http://0.0.0.0:8000
- Для работы с API рекомендуется использовать Postman либо иную аналогичную программу (https://www.postman.com/downloads/)
