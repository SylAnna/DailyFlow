from django.db import models
from django.utils import timezone

# Create your models here.

# Models for Cateogry
class Category(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=7, default="#000000") 

    def __str__(self):
        return self.name

# Models For List
class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.item + ' | ' + str(self.completed)