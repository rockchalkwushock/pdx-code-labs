from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from datetime import datetime

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    checked_out = models.BooleanField(default=False)
    published_date = models.DateTimeField(default=datetime.now())
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Card(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    checked_out = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.book} {self.timestamp}'
