# Create your models here.
from django.db import models
import time
import datetime


# Create your models here.
class Usergroup(models.Model):
    ID=models.IntegerField(primary_key=True)
    groupname=models.CharField(max_length=30)
    username=models.TextField()
class User(models.Model):
    ID=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=30)
    telephone=models.CharField(max_length=30)
    userhost=models.TextField()
class Host(models.Model):
    ID = models.IntegerField(primary_key=True)
    Host=models.CharField(max_length=30)
    services=models.TextField()

class Table(models.Model):
    id = models.IntegerField(primary_key=True)
    hostip=models.CharField(max_length=30)
    service=models.CharField(max_length=30)
    date=models.TextField()
    sendtime=models.CharField(max_length=30)
