from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

# Create your models here.
class User(AbstractUser):
    pass

class hotels_listings(models.Model):
    hotel_chain_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=200)
    rating = models.IntegerField()
    image_url = models.URLField(max_length=500, blank=True)
    objects = models.Manager()

    def __str__(self):
        return f"{self.hotel_chain_name} : {self.rating}"
    
    def getRangeRating(self):
        return range(self.rating)