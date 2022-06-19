from django.db import models
from django.urls import reverse

# 1. https://www.youtube.com/watch?v=Sut1s4LdMG0 - работа с админ панелью
# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=256, verbose_name='Имя')
    last_name = models.CharField(max_length=256, verbose_name='Фамилия')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст')

    def __str__(self):             # [1]
        return self.last_name
    
    class Meta:                      # [1]
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ['last_name']  # '-' обратная сортировка

    def toDictionary(self):
        """
        A utility function to convert object of type Book to a Python Dictionary
        """
        output = {}
        output["pk"] = self.pk
        output["first_name"] = self.first_name
        output["last_name"] = self.last_name
        output["age"] = self.age
    
        return output

    
class Book(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    released_year = models.SmallIntegerField(verbose_name='Год издания')
    description = models.TextField(verbose_name='Описание')
    author_id = models.ForeignKey(Author, on_delete = models.PROTECT)

    def get_absolute_url(self):
        return reverse('books', kwargs={'book_id': self.pk})

    def __str__(self):             # [1]
        return self.title

    class Meta:                      # [1]        
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ['title']


    def toDictionary(self):
        """
        A utility function to convert object of type Book to a Python Dictionary
        """
        output = {}
        output["pk"] = self.pk
        output["title"] = self.title
        output["description"] = self.description
        output["released_year"] = self.released_year
        output["author_id"] = self.author_id.pk
    
        return output

