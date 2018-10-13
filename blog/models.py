from django.db import models
from django.utils.timezone import datetime

# Create your models here.

class Catagory(models.Model):
    catagory_name = models.CharField(max_length=100)
    is_active = models.BooleanField()

    def __str__(self):
        return self.catagory_name

class BlogPost(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_description = models.CharField(max_length=200)
    blog_date = models.DateTimeField('Publish date')
    blog_author = models.CharField(max_length=100)


    def __str__(self):
        return self.blog_title

