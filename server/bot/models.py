from django.db import models
from django.contrib.models.auth import User

# Create your models here.


class Patient(models.Model):
    number = models.CharField(max_length=20)


class Nurse(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
