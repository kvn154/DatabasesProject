from django.contrib import admin
from .models import User, hotels_listings
# Register your models here.

admin.site.register(User)
admin.site.register(hotels_listings)
