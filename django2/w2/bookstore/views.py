from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# создание динамических ссылок
# https://proproprogs.ru/django/formirovanie-url-adresov-v-shablonah

# Create your views here.
def books(request):
    ans= Book.objects.all()
    books = []
    for i in ans:
        books.append(i.toDictionary())      # Converting `QuerySet` to a Python Dictionary

    return render(request,'bookstore/templates/books.html', context = {'books':books} )


def book_description(request, book_id):
    book = Book.objects.get(id = book_id).toDictionary()
    return render(request,'bookstore/templates/book_description.html', context = book )

def author(request, author_id):
    #output = f"<h2>Author ID = {author_id}</h2>"
    #return HttpResponse(output)
    ans = Book.objects.filter(author_id = author_id)
    author = Author.objects.get(id = author_id).toDictionary()
    books = []
    for i in ans:
        books.append(i.toDictionary())      # Converting `QuerySet` to a Python Dictionary

    data = {'author': author, 'books': books}
    print(data)
    return render(request,'bookstore/templates/author.html', context = data )
