from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#카테고리
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)


# 상품 아이템
class Item(models.Model):
    name = models.CharField(max_length=30, unique=True)
    content = models.CharField(max_length=30, unique=True)
    image = models.ImageField(upload_to='post/images/%Y/%m/%d/', blank=True)
    price = models.IntegerField()

    delivery_price = models.IntegerField()

    manufacture = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    #item = models.ManyToManyField( blank=True)

class Manufacture(models.Model):
    name = models.CharField(max_length=30, unique=True)
    address = models.TextField()
    number = models.IntegerField()

    area = models.TextField()
