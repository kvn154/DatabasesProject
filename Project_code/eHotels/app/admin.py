from django.contrib import admin
from .models import  *
# Register your models here.

admin.site.register(User)
admin.site.register(hotel)
admin.site.register(hotel_chain)
admin.site.register(capacity)
admin.site.register(room)



