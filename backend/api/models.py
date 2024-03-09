from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=500)
    price = models.FloatField()
    img = models.CharField(max_length=10000)
    discount = models.FloatField()
    rating = models.FloatField()
    link = models.CharField(max_length=10000)
    reviews = models.TextField()
    description = models.TextField()


class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)


class Comparison(models.Model):
    product1 = models.IntegerField()
    product2 = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

# class Wishlist(models.Model):

