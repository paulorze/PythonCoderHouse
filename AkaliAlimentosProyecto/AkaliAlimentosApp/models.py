from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20, unique = True)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30, unique = True)
    address = models.CharField(max_length=30)
    admin = models.BooleanField(default=True)

class Product(models.Model):
    name = models.CharField(max_length=20, unique = True)
    category = models.CharField(max_length=20)
    description = models.CharField(max_length=400)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField()
    nationality = models.CharField(max_length=20)

class Order(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    products = models.ManyToManyField(Product, through='OrderToProduct')
    purchase_time = models.DateTimeField(auto_now_add=True)

class OrderToProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField()
