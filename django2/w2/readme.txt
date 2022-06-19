Задание 1

В созданном проекте создайте приложение firstapp;
добавьте в него файл urls.py;
создайте urlpattern;
подключите к этому url адресу функцию обработчик hellodjango;
реализуйте функцию hellodjango, чтобы она с помощью метода HttpResponse по пустому url выводила в браузер фразу "Hello Django!".


Задание 2

Создайте url path("<str:name>/"), и функцию обработчик которая будет выводить в браузер f"Hello {name}!"



Задание 3

Создайте обработчики, чтобы:

по url “date/” выводил дату (22.03.2022);
по url “date/year/” выводил 2022, по url “date/day/” выводил 22;
по url “date/month/” выводил 03.

==============
продолжение

Задание 1

В созданном проекте создайте приложение bookstore;



Задание 2

создайте два массива books и authors и заполните их, пример ,books = [{'id': 1, 'title': 'Fluent Python','released_year': 2015, 'description': 'Python’s simplicity lets you become productive quickly, but this often means you aren’t using everything it has to offer. With this hands-on guide, you’ll learn how to write effective, idiomatic Python code by leveraging its best—and possibly most neglected—features. Author Luciano Ramalho takes you through Python’s core language features and libraries, and shows you how to make your code shorter, faster, and more readable at the same time.', 'author_id': 1}, {...}, ...], authors = [{'id': 1, 'first_name': 'Luciano', 'last_name': 'Ramalho', 'age': 51 }, {...}, ...]



Задание 3

создайте базовый юрл и функцию представление которая будет выводить список всех книг, а также в каждой книге должна быть ссылка на полное описание книги



Задание 4

создайте юрл и функцию представление которая будет отображать данные одной книги, в ней должны быть две ссылки на инфо по автору, и на базовую страницу (список книг)



Задание 5

создайте юрл и функцию представление которая будет отображать данные автора, в ней должны быть две ссылки на список книг автором которых является, и на базовую страницу (список книг)