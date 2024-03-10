from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    website = models.TextField(max_length=1000)
    title = models.CharField(max_length=255)
    price = models.FloatField()
    img = models.CharField(max_length=10000)
    description = models.TextField()
    discount = models.FloatField()
    about = models.TextField(max_length = 1000)
    rating = models.FloatField()
    link = models.TextField(max_length=1000)
    variant = models.CharField(max_length = 255)
    offers = models.TextField(max_length = 1000)
    options = models.TextField(max_length = 1000)
    reviews = models.TextField(max_length=1000)


class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'query')


class Comparison(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product1 = models.IntegerField()
    product2 = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    product = models.IntegerField(null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')


