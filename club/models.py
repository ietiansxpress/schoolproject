#from _typeshed import Self
from django.db import models

class Resister(models.Model):
    name = models.CharField(max_length=30)
    school= models.CharField(max_length=40)
    phone=models.CharField(max_length=10)

    def __str__(self):
     return self.name +"-" + self.phone


# Create your models