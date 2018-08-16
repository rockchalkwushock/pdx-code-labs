from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    body = models.TextField()
    timestamp = models.DateTimeField(default=datetime.now)
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.body
