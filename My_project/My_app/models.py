from django.db import models

# Create your models here.

class details(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.CharField(max_length=50)
    year_of_joining = models.IntegerField()
    rollno = models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=15)
    place = models.CharField(max_length=50)
