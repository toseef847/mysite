from django.db import models

# Create your models here.

class Class(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Subject(models.Model):
    code = models.CharField(max_length = 20)
    name = models.CharField(max_length = 200)
    _class = models.ForeignKey(Class, on_delete=models.CASCADE, blank=True)
    def __str__(self):
        return self.name
