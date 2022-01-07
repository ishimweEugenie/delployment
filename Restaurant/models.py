from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User


# Create your models here.



class District(models.Model):
    Di_name = models.CharField(max_length=50)
    provinse = models.CharField(max_length=100)

    def __str__(self):
        return self.Di_name


class Dishes(models.Model):
    Dish_name = models.CharField(max_length=100)
    price = models.IntegerField()
    co_time = models.DateTimeField(auto_now=True)
    ingredients = models.TextField(blank=True)
    pictures = models.ImageField()

    def __str__(self):
        return self.Dish_name


class Sector(models.Model):
    sec_name = models.CharField(max_length=50)
    disstrict = models.CharField(max_length=50)
    province = models.CharField(max_length=100)

    def __str__(self):
        return self.sec_name


class Resto(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    rating = models.IntegerField()
    dishe = models.ForeignKey(Dishes, on_delete=models.PROTECT, null=True, related_name="dishes")
    district = models.ForeignKey(District, on_delete=models.PROTECT, blank=True, null=True, related_name="address")
    sector = models.ForeignKey(Sector, on_delete=models.PROTECT, blank=True, null=True, related_name="address")

    def __str__(self):
        return f"{self.name} {self.rating} {self.owner}"

