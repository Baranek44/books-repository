from django.db import models
from django.forms import CharField

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=80)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title