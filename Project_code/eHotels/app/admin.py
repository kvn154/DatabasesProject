from django.contrib import admin
from .models import  *
# Register your models here.

admin.site.register(User)
admin.site.register(hotel)
admin.site.register(hotel_chain)
admin.site.register(capacity)
admin.site.register(room)
admin.site.register(payement)
admin.site.register(client)
admin.site.register(payement_for)
admin.site.register(reservation)
admin.site.register(card)
admin.site.register(employee)
admin.site.register(works_for)
admin.site.register(reservation_archive)
admin.site.register(location)


