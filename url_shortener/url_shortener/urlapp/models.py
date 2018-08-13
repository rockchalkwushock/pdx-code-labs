from django.db import models
from uuid import uuid4
from datetime import datetime

# Create your models here.


class Url(models.Model):
    code = models.UUIDField(default=uuid4, editable=False)
    created_date = models.DateTimeField(default=datetime.now())
    url = models.URLField()

    def __str__(self):
        return self.code
