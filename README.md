# db-hack
Данный скрипт предназачен для того, чтобы вы могли редактировать свой 
элементронный дневник! А именно: исправлять плохие оценки, удалять гневные 
комментарии учителей и даже добавлять себе комментарии с похвалой! 

## Запуск

- Скачайте файл со скриптом.
- Скрипт нужно залить на сервер сайта, положить в корневую папку рядом с 
  manage.py. 
- Если вы не хотите работать с сайтом на сервере, вы можете развернуть сайт 
  у себя и проводить все теже самые манипуляции на локальном 
  компьютере. Как это сделать и как потом запустить сайта можно посмотреть 
  в [README](https://github.com/devmanorg/e-diary/blob/master/README.md) 
  сайта  электронного дневника. 
- В корневой папке сайта должен быть файл БД.
- Если его нет, вы можете добавить туда свой подготовленный файл с БД.
- Далее нужно, находясь в корневой папке сайта, открыть терминал и ввести 
  команду:

      python manage.py shell 

- Далее в интерактивную оболочки Питону, нужно импортировать функции из 
  данного скрипта (можно все сразу, можно какие-то отдельные):

      from scripts import *

В файле scripts доступны 3 функции: 
- `fix_marks(schoolkid)` - функция исправляет 2 и 3, на 4 или 5. Принимает 
  один аргумент: schoolkid - ФИО ученика. Во всех функциях ФИО вводится в 
  соответсвующем порядке.
- `remove_chastisements(schoolkid)` - функция удаляет жалобы учителей. 
  Принимает один аргумент: schoolkid - ФИО ученика. 
- `create_commendation(schoolkid, subject)` - функция создаёт запись с 
  похвалой от учителя. Принимает два аргумента: schoolkid - ФИО ученика и 
  subject - предмет, по которому нужна похвала от учителя.

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке 
на сайте [Devman](https://dvmn.org).


