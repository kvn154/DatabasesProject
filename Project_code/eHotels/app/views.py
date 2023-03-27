from django.shortcuts import render
from .models import hotel, hotel_chain

# Create your views here.
def index(request):
    hotels_listing = hotel.objects.all().order_by('-rating')
    return render(request, "index.html",{
        "hotels_listings": hotels_listing
    })

def hotel_chains_listing(request):
    hotels_chain_listings = hotel_chain.objects.all().order_by('-rating')
    return render(request, "index.html",{
        "hotels_listings": hotels_chain_listings
    })