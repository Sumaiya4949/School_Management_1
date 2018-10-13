from django.db import models

# Create your models here.
class District(models.Model):
    distric_name = models.CharField(max_length = 100)
    distric_area = models.IntegerField()
    distric_population = models.IntegerField()
    def __str__(self):
        return self.distric_name

class UserInfo(models.Model):
    user_name = models.CharField(max_length=100)
    user_age = models.IntegerField()
    gender_choice = (('m','male'),('f','female'))
    user_gender = models.CharField(max_length=50,choices=gender_choice)
    def __str__(self):
        return self.user_name


    
