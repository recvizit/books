from django.db import models


class Author(models.Model):

    name = models.CharField(max_length=256)
    pic = models.ImageField(upload_to='author_pics/%Y/%m/')
    bio = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.TextField()
    author = models.ManyToManyField(Author)
    year = models.IntegerField()
    pic = models.FileField(upload_to='ebook/%Y')
    ebook = models.FileField(upload_to='ebook/%Y')

    def __str__(self):
        return self.title


class Shelf(models.Model):
    location = models.SlugField(default='')
    load = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.location
