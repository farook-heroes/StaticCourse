from django.db import models

# Create your models here.

class Product(models.Model):
    id    = models.AutoField(primary_key=True)
    name  = models.CharField(max_length = 100) 
    info  = models.CharField(max_length = 100, default = '')
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name



class Student(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    age = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    about_info = models.TextField(blank=True)

    def __str__(self):
        return self.username
    
class Teacher(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    age = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    about_info = models.TextField(blank=True)

    def __str__(self):
        return self.username


