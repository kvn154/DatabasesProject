from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here..
class User(AbstractUser):
    pass

class hotel_chain(models.Model):
    chain_id = models.IntegerField(primary_key=True)
    addressArray = ArrayField(models.CharField(max_length=150))
    name = models.CharField(max_length=150)
    nTelephones = ArrayField(models.CharField(max_length=30))
    email = models.CharField(max_length=150)
    rating = models.IntegerField()
    image_url = models.URLField(max_length=500, blank=True, null= True)
    numberOfHotels = models.IntegerField(default=0)
    objects = models.Manager()

    def __str__(self):
        return f"{self.chain_id}_{self.name} : {self.rating}"
    
class hotel(models.Model):
    hotel_id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=150)
    zone = models.CharField(max_length=150)
    chain_id = models.ForeignKey(hotel_chain, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    nTelephones = ArrayField(models.CharField(max_length=30))
    email = models.CharField(max_length=150)
    rating = models.IntegerField()
    image_url = models.URLField(max_length=500, blank=True, null= True)
    numberOfRooms = models.IntegerField(default=0)
    objects = models.Manager()
    def __str__(self):
        return f"{self.hotel_id}_{self.name} : {self.rating}"
    
class capacity(models.Model):
    id = models.IntegerField(primary_key=True)
    capacity = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.id} : {self.capacity}"

class room(models.Model):
    class Meta:
        unique_together = (('room_number', 'hotel_id'),)
    room_number = models.IntegerField()
    hotel_id = models.ForeignKey(hotel, on_delete=models.CASCADE)
    capacity = models.ForeignKey(capacity, on_delete=models.CASCADE)
    extrabed = models.BooleanField()
    price = models.DecimalField(max_digits= 20, decimal_places=2)
    view = ArrayField(models.CharField(max_length=50, blank=True, null=True))
    def __str__(self):
        return f"{self.hotel_id.name}_{self.room_number} : {self.capacity}"


