from django.db import models

# Create your models here.

class working_data(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    items = models.TextField()
    