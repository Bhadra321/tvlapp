from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Apartment(models.Model):
    name=models.CharField(max_length=30)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()


    def  __str__(self):
        return self.name

class Users(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.IntegerField()
    place=models.CharField(max_length=50) 

class Register(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    email=models.EmailField()
    regno=models.CharField(max_length=20)
    phone=models.CharField(max_length=15)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=100)
    Value=models.IntegerField()
    user_type=models.CharField(max_length=10)       