from django.contrib import admin

from shelf.models import Book, Author, Shelf

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Shelf)
