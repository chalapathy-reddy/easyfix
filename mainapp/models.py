from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User


class employee(Model):
    username = models.CharField(max_length=25)
    email = models.EmailField(unique=True, max_length=30)
    password = models.CharField(max_length=256)
    qualification = models.CharField(max_length=25)
    phone = models.CharField(max_length=15)
    work = models.IntegerField(default=0)


class service(Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    address = models.TextField()
    employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    date = models.DateField(default=None)
    done = models.BooleanField(default=False);


class product(Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField(max_length=25)
    company = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
