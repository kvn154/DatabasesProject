"""eHotels URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hotel_chains", views.hotel_chains_listing, name="hotel_chains"),
    path("<int:id>", views.hotel_for_hotel_chain, name = "hotel_for_hotel_chain"),
    path('admin/', admin.site.urls),
    path("categories", views.category, name="categories"),
    path("zones", views.zones, name="zones"),
    path("category=<int:category>", views.list_category, name="list_category"),
    path("zone=<str:zone>", views.list_zone, name="list_zone"),
    path("reserve=<int:h_id>", views.start_reservation, name="reservation"),
    path("reserve_employee=<int:h_id>", views.start_reservation_employee, name="reservation_employee"),
    path("choose_room=<int:h_id>", views.choose_room, name="choose_room"),
    path("choose_room_employee=<int:h_id>", views.choose_room_employee, name="choose_room_employee"),
    path("complete_reservation=<int:h_id>", views.complete_reservation, name="complete_reservation"),
    path("complete_reservation_employee=<int:h_id>", views.complete_reservation_employee, name="complete_reservation_employee"),
    path("save_reservation=<int:h_id>", views.save_reservation, name="save_reservation"),
    path("save_reservation_employee=<int:h_id>", views.save_reservation_employee, name="save_reservation_employee"),
    path("employee", views.index_employee, name="index_employee"),
    path("login", views.login_employee, name="login"),
    path("logout", views.logout_employee, name="logout"),
    path("reservation_listing", views.reservation_listing, name="reservation_listing"),
    path("location=<int:r_id>", views.location_employee , name="location"),
    path("save_location=<int:r_id>", views.save_location, name="save_location"),


]
