from django.contrib import admin
# 1. https://www.youtube.com/watch?v=Sut1s4LdMG0 - работа с админ панелью
# Register your models here.
from .models import *

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'released_year', 'description')
    list_display_links = ('id',)
    search_fields = ('title',)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'age')
    list_display_links = ('id',)
    search_fields = ('first_name',)

admin.site.register(Author, AuthorAdmin)        #[1]
admin.site.register(Book, BookAdmin)          #[1]
