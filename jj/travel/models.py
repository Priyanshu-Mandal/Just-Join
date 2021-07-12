from django.db import models
from django.db.models.manager import ManagerDescriptor

# Create your models here.


class user(models.Model):
    name=models.CharField(max_length=30)
    phno=models.IntegerField()
    email=models.EmailField()
    username=models.CharField(primary_key=True,max_length=10)
    password=models.CharField(max_length=10)

class travel(models.Model):
    username=models.ForeignKey(user, on_delete=models.CASCADE)
    start=models.CharField(max_length=30)
    end=models.CharField(max_length=30)
    pin=models.IntegerField()
    seats=models.IntegerField()
    date=models.DateField(auto_now=False)

