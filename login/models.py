from django.db import models

# Create your models here.
class User(models.Model):
    email=models.EmailField(max_length=80)
    contact=models.CharField(max_length=10)
    uname=models.CharField(max_length=20)
    password=models.CharField(max_length=15)