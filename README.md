# Тестовое задание на позицию python-разработчик в компанию DataFort

_Сервис по сбору информации о показателях климатических условий заданных мест для дальнейшего использования в задачах компании._

_Информация собирается с сайта https://openweathermap.org/ для 50 самых больших городов мира.
Запись в базу данных производтся каждый час._

----
### Список городов
Список городов собирается с заданного файла с данными.
Для каждого города сохраняется:
- Название;
- Координата сверной широты;
- Координата восточной долготы;
- Численность населения.
----
### Погодные характеристики
Сайт https://openweathermap.org/ позволяет получить большое количетсво параметров климатических условий.
В настоящем проекте для каждого города, по заданным координатам, сохряняются следующие данные (_текущие значения на время сохранения_):
- Температура воздуха;
- Темперутара воздуха "по ощущениям";
- Влажность воздуха.

Все данные передаются серверу в метрической системе. 

----
### Настройки админки
В админ-зоне выведена вся сохраняемая в базу данных информация по выбранным городам и полученным показателям климатических параметров.
#### Модель городов
- Выведен список городов, со значениями широты, долготы и численности населения;
- С помощью фильтра выбраются конкретные города.
#### Модель погоды
- Выведен список климатических параметров, такие как температура, температура по ошущениям и влажность. Для каждой строчки есть ссылка на город;
- С помощью фильтра выбраются конкретные города.
----

### Инфраструктура
- База данных **PostgeSQL**
- - Данная база данных выбрана как одна из самых удобных и популярных баз реляционного типа (_и автору она привычнее_);
- - В проекте использованы две таблицы. Основая с информацие о погоде и дополнительная с информацией о городах. Данная структура является самой удобной, отвечающей поставленной задаче;
- Язык програмирования и версия **Python 3.9**
- - Данная версия языка поддерживает все необходимые версии библиотек, нововведения в версиях 3.10 и 3.11 на данном этапе работ не используются и не планируется, перевести сервис на более свежую версию языка не составит труда (_ну и автора эта версия стоит на локальной машине_);
- Фраемворк и версия **Django 4.1.3**
- - Выбор фраемворка обусловлен лишь стеком автора. *Возможно в дальнейшем развитие проекта следует предусмотреть "переезд" на FastApi*;
- Библиотека **schedule**
- - Для периодического обращения сервиса для получения данных о погоде использованная библиотека schedule, позволяющая настроить расписание работы необхолимых функций;
----

### Ограничения

- Получение данных о городах из файла с данными. Частично преодолевается добавлением информации о городах через админку
- Отсутствие требования о сроках хранения данных о температуре. Необходимо предусмотреть срок и удалять из базы устаревшие данные
- Библиотека *schedule*. При расширении проекта и увеличении функциональности следует предусмотреть переход на *celery*
- Сайт, предоставляющий информация о погоде. В бесплатный тариф входит ограниченное количество запросов и предстовляемых данных. _Для решения поставленной задачи данный тариф подходит_

### Инструкция по запуску

-