from django.db import models
from django.urls import reverse

class stud(models.Model):
    name = models.CharField(max_length=50, unique=True)
    age = models.PositiveIntegerField()
    std = models.CharField(max_length=9)