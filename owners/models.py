from django.db import models

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    age = models.IntegerField()

class Dog(models.Model):
    name = models.CharField(max_length=45)
    age = models.IntegerField()
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
