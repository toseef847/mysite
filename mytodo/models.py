from django.db import models
from datetime import datetime

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    date = models.DateTimeField(default = datetime.now, blank=True)
    completed = models.BooleanField(default = False)

    def __str__(self):
        return self.title
