from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=50)
    addres = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name