from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    is_new_customer_renamed = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class FoodItem(models.Model):
    name = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer)
    food_items = models.ManyToManyField(FoodItem, through='OrderItemRelationship')
    created_at = models.DateTimeField()
    delivery_at = models.DateTimeField()


class OrderItemRelationship(models.Model):
    order = models.ForeignKey(Order)
    food_item = models.ForeignKey(FoodItem)
    quantity = models.IntegerField()
    special_instructions = models.CharField(max_length=200)
    subtotal = models.FloatField()


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)


class Menu(models.Model):
    food_items = models.ManyToManyField(FoodItem)
    name = models.CharField(max_length=200)
    restaurant = models.ForeignKey(Restaurant)
