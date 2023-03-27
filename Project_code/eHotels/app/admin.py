from django.contrib import admin
from .models import User, hotel, hotel_chain
# Register your models here.

admin.site.register(User)
admin.site.register(hotel)
admin.site.register(hotel_chain)


