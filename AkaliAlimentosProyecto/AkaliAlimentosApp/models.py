from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=20, unique = True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30, unique = True)
    address = models.CharField(max_length=30)
    # admin = models.BooleanField(default = False)
    # is_staff= models.BooleanField(default = False)
    # is_superuser = models.BooleanField(default = False)

class Product(models.Model):
    name = models.CharField(max_length=40, unique = True)
    category = models.CharField(max_length=20)
    short_description = models.CharField(max_length=40, default = 'Producto de Akali Alimentos')
    description = models.CharField(max_length=400)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField()
    nationality = models.CharField(max_length=20)
    img = models.CharField(max_length=150, default = "{% static 'assets/img/icono_placeholder.png' %}")

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    productlist = models.ManyToManyField('CartToProduct', related_name='productlist')

class CartToProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE, default = 1)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity  = models.PositiveIntegerField()

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

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    body = models.CharField(max_length=500)