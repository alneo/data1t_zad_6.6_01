# Промежуточная аттестация 6.10
![GitHub top language](https://img.shields.io/github/languages/top/alneo/data1t_zad_6.6_01)
![GitHub issues](https://img.shields.io/github/issues/alneo/data1t_zad_6.6_01)

## PostgreSQL - Python - docker compose

## Задание:
- Представим, что Вы попали в очень классную компанию, в которой пока что только создается инфраструктура. Так как Вы пока находитесь на испытательном сроке, Вам дали задачу на знание docker compose.
Необходимо создать 2 контейнера: в первом разворачивается PostgreSQL, а во втором  — Python.

### Вот что необходимо сделать:

- Развернуть базу данных PostgreSQL ваша_фамилия и создать таблицу test_table. Таблица должна создаваться автоматически при развертывании docker compose из файла init.sql (этот файл тоже необходимо создать).

- Таблица должна содержать 4 столбца: name, surname, city, age. name — от 4 до 10 символов, surname — без разницы, city — без разницы, age — только положительные числа, до 150. Количество строк — не менее 20. init.sql должен содержать ключевые слова CREATE и INSERT.

- Выполнить запрос к таблице на Python (используйте psycopg2), который покажет максимальный и минимальный возраст для имен, длина которых меньше 6 символов.

- Получившийся результат должен выводиться в терминале docker при запуске образа. 

## Результат
В качестве решения необходимо прислать ссылку на свой git-репозиторий (GitHub, GitLab и т.п.) со всеми файлами задания. При запуске контейнера необходимо, чтобы создавалась БД, таблица, были тестовые данные, а также в терминале выводился ответ на пункт 4.

## Ответ
- Ссылка на DockerHub ```https://hub.docker.com/r/alneoru/data1t_itog``` 

