from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

# Create your models here.
class User(AbstractUser):
    pass


class hotel_chain(models.Model):
    chain_id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    nTelephone = models.CharField(max_length=20)
    rating = models.IntegerField()
    image_url = models.URLField(max_length=500, blank=True)
    objects = models.Manager()

    def __str__(self):
        return f"{self.name} : {self.rating}"
    
class hotel(models.Model):
    hotel_id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=150)
    chain_id = models.ForeignKey(hotel_chain, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    nTelephone = models.CharField(max_length=20)
    rating = models.IntegerField()
    image_url = models.URLField(max_length=500, blank=True)
    objects = models.Manager()
    

    def __str__(self):
        return f"{self.name} : {self.rating}"
