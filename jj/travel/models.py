from django.db import models
from django.db.models.manager import ManagerDescriptor

# Create your models here.


class user(models.Model):
    name=models.CharField(max_length=30)
    phno=models.CharField(max_length=15)
    email=models.EmailField()
    username=models.CharField(primary_key=True,max_length=30)
    password=models.CharField(max_length=10)

class travel(models.Model):
    username=models.ForeignKey(user, on_delete=models.CASCADE)
    startp=models.IntegerField()
    endp=models.IntegerField()
    seats=models.IntegerField()

