from django.db import models
from datetime import datetime

# Create your models here.
class SchoolInfo(models.Model):
    name = models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    phone = models.IntegerField()
    district = models.CharField(max_length=100)
    address = models.TextField()
    stablished_date = models.DateTimeField()
    def __str__(self):
        return self.name
