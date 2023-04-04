from datetime import datetime
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
    view = ArrayField(models.CharField(max_length=50, blank=True, null=True), null=True)
    def __str__(self):
        return f"{self.hotel_id.name}_{self.room_number} : {self.capacity}"
    def __eq__(self, other):
        return self.capacity == other.capacity and self.extrabed == other.extrabed and self.price == other.price and set(self.view) == set(other.view)

class client(models.Model):
    ssa = models.CharField(max_length = 100,primary_key=True)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    def __str__(self):
            return f"{self.first_name}_{self.last_name} : {self.ssa}"
    
class card(models.Model):
    card_number = models.CharField(max_length = 25,primary_key=True)
    expiry_date = models.CharField(max_length=8)
    cvv = models.CharField(max_length=4)
    name_on_the_card = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.card_number}"

class payement(models.Model):
    card_info = models.ForeignKey(card, on_delete=models.CASCADE, blank=True, null=False)
    amount =  models.DecimalField(max_digits= 20, decimal_places=2)
    client = models.ForeignKey(client, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.client.first_name} {self.client.last_name} : ${self.amount}"

class reservation(models.Model):
    id = models.AutoField(primary_key=True)
    date_of_reservation = models.DateField(blank=True)
    start_time = models.DateField()
    end_time = models.DateField()
    client = models.ForeignKey(client, on_delete=models.CASCADE)
    hotel = models.ForeignKey(hotel, on_delete=models.CASCADE)
    view = ArrayField(models.CharField(max_length=50, blank=True, null=True), null=True)
    capacity = models.ForeignKey(capacity, on_delete=models.CASCADE)
    extrabed = models.BooleanField()
    price = models.DecimalField(max_digits= 20, decimal_places=2)
    def __str__(self):
        return f"{self.client.first_name} {self.client.last_name} : {self.capacity.capacity} - ${self.price}"
    
class payement_for(models.Model):
    id = models.AutoField(primary_key=True)
    reservation = models.ForeignKey(reservation, on_delete=models.CASCADE)
    payement = models.ForeignKey(payement, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.reservation.client.first_name} {self.reservation.client.last_name} : {self.reservation.capacity.capacity} - ${self.reservation.price}"

class commodity(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    room = models.ForeignKey(room, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.room} : {self.type}"
    
class damage(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=250)
    room = models.ForeignKey(room, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.room} : {self.description}"


