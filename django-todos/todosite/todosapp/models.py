from django.db import models
from datetime import datetime
# Create your models here.


class Todo(models.Model):
    todo_text = models.CharField(max_length=250, unique=True)
    created_date = models.DateTimeField(default=datetime.now())
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.todo_text
