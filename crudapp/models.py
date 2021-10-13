from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    roll = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

class subject(models.Model):
    stu_id=models.ForeignKey(Student, on_delete=models.CASCADE)
    CourseName = models.CharField(max_length=250)
    credithours = models.IntegerField()
    


    