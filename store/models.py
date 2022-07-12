from contextlib import nullcontext
from pickle import TRUE
from statistics import harmonic_mean
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#customer class created
class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.name

#order class created
class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

#product class created
class Product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

#shipping address class created
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, models.SET_NULL, null=True)
    order = models.ForeignKey(Order, models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=300, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

#order item class created
class OrderItem(models.Model):
    product = models.ForeignKey(Product, models.SET_NULL, null=True)
    order = models.ForeignKey(Order, models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price*self.quantity
        return total
