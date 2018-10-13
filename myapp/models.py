from django.db import models




class ScoreRecord(models.Model):
    student_roll = models.IntegerField(unique=True)
    student_gpa = models.FloatField()
    student_year = models.IntegerField()
    student_class = models.IntegerField()
    student_exam = models.CharField(max_length=20)

    def __str__(self):
        return str(self.student_roll)

class Class_wise(models.Model):
    class_id = models.IntegerField(unique=True)
    class_name = models.CharField(max_length=20)
    def __str__(self):
        return str(self.class_id)

class Gurdian(models.Model):

    gurdian_name = models.CharField(max_length=50)
    gender_choose = (('m','male'),('f','female'))
    gurdian_gender = models.CharField(max_length=50,choices = gender_choose)
    gurdian_age = models.IntegerField()
    gurdian_phone = models.IntegerField(unique=True)

    def __str__(self):
        return self.gurdian_name

class StudenInfo(models.Model):

    name = models.CharField(max_length=50)
    roll = models.IntegerField(unique=True)
    std_class = models.IntegerField()
    gender_choice = (('m', 'male'), ('f', 'female'))
    gender = models.CharField(max_length=50, choices=gender_choice)
    age = models.IntegerField()
    guard = models.OneToOneField(Gurdian, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
            return self.name
