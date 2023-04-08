
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db import IntegrityError


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
    def save(self, *args, **kwargs):
         if not self.image_url:
              self.image_url = None
         super(hotel_chain, self).save(*args, **kwargs)
    
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
    def save(self, *args, **kwargs):
         if not self.image_url:
              self.image_url = None
         super(hotel, self).save(*args, **kwargs)
    
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
    view = ArrayField(models.CharField(max_length=50, blank=True, null=True), null=True, blank=True)
    def __str__(self):
        return f"{self.hotel_id.name}_{self.room_number} : {self.capacity}"
    def __eq__(self, other):
        return self.capacity == other.capacity and self.extrabed == other.extrabed and self.price == other.price and set(self.view) == set(other.view)
    def save(self, *args, **kwargs):
         if not self.view:
              self.view = None
         super(room, self).save(*args, **kwargs)

class client(models.Model):
    ssa = models.CharField(max_length = 100,primary_key=True)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    def __str__(self):
            return f"{self.first_name}_{self.last_name} : {self.ssa}"
    def save(self, *args, **kwargs):
         if not self.middle_name:
              self.middle_name = None
         super(client, self).save(*args, **kwargs)
    
class card(models.Model):
    card_number = models.CharField(max_length = 25,primary_key=True)
    expiry_date = models.CharField(max_length=8)
    cvv = models.CharField(max_length=4)
    name_on_the_card = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.card_number}"

class payement(models.Model):
    card_info = models.ForeignKey(card, on_delete=models.CASCADE, blank=True, null=True)
    amount =  models.DecimalField(max_digits= 20, decimal_places=2)
    client = models.ForeignKey(client, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.client.first_name} {self.client.last_name} : ${self.amount}"
    def save(self, *args, **kwargs):
         if not self.card_info:
              self.card_info = None
         super(payement, self).save(*args, **kwargs)

class reservation(models.Model):
    id = models.AutoField(primary_key=True)
    date_of_reservation = models.DateField(blank=True)
    start_time = models.DateField()
    end_time = models.DateField()
    client = models.ForeignKey(client, on_delete=models.CASCADE)
    hotel = models.ForeignKey(hotel, on_delete=models.CASCADE)
    view = ArrayField(models.CharField(max_length=50, blank=True, null=True), null=True, blank=True)
    capacity = models.ForeignKey(capacity, on_delete=models.CASCADE)
    extrabed = models.BooleanField()
    price = models.DecimalField(max_digits= 20, decimal_places=2)
    def __str__(self):
        return f"{self.client.first_name} {self.client.last_name} : {self.capacity.capacity} - ${self.price}"
    def save(self, *args, **kwargs):
         if not self.view:
              self.view = None
         super(reservation, self).save(*args, **kwargs)

class reservation_archive(models.Model):
    id = models.IntegerField(primary_key=True)
    date_of_reservation = models.DateField(blank=True)
    start_time = models.DateField()
    end_time = models.DateField()
    client_id = models.CharField(max_length = 100)
    hotel_id = models.IntegerField()
    view = ArrayField(models.CharField(max_length=50, blank=True, null=True), null=True, blank=True)
    capacity_id = models.IntegerField()
    extrabed = models.BooleanField()
    price = models.DecimalField(max_digits= 20, decimal_places=2)
    def __str__(self):
        return f"{self.client_id}: {self.capacity_id} - ${self.price}"
    def save(self, *args, **kwargs):
         if not self.view:
              self.view = None
         super(reservation, self).save(*args, **kwargs)
    class Meta:
        managed = False
        db_table = 'app_reservation_archive'

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

class employee(models.Model):
    ssa = models.CharField(max_length = 100,primary_key=True)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20)
    post = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    def __str__(self):
            return f"{self.first_name}_{self.last_name} : {self.ssa}"
    
    def delete(self, *args, **kwargs):
        old_user = User.objects.get(username = self.ssa)
        old_user.delete()
        super(employee, self).delete(*args, **kwargs)
    def save(self, *args, **kwargs):
        if not self.middle_name:
            self.middle_name = None
        user = User.objects.raw(f"Select * from app_user where id  = {self.ssa}")
        if len(user) == 0:
            user = User.objects.create_user(username = self.ssa, password =  self.password)
            user.save()
        else:
            old_user = User.objects.get(username = self.ssa)
            old_user.delete()
            user = User.objects.create_user(username = self.ssa, password =  self.password)
            user.save()
        self.password = user.password
        super(employee, self).save(*args, **kwargs)
        

class works_for(models.Model):
    id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    hotel = models.ForeignKey(hotel, on_delete=models.CASCADE)
    def __str__(self):
            return f"{self.employee.first_name}_{self.employee.last_name} works for {self.hotel.name}"


class location(models.Model):
    reservation = models.ForeignKey(reservation, on_delete=models.CASCADE)
    room = models.ForeignKey(room, on_delete=models.CASCADE)
    employee = models.ForeignKey(employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.reservation} : {self.room} made by {self.employee.first_name}_{self.employee.last_name}"
