from django.shortcuts import render
from .models import hotel, hotel_chain

# Create your views here.
def index(request):
    hotels_listing = hotel.objects.raw('SELECT * FROM app_hotel ORDER BY rating DESC')
    return render(request, "index.html",{
        "hotels_listings": hotels_listing
    })

def hotel_chains_listing(request):
    hotels_chain_listings = hotel_chain.objects.raw('SELECT * FROM app_hotel_chain ORDER BY rating DESC')
    return render(request, "index.html",{
        "hotels_listings": hotels_chain_listings
    })

def hotel_for_hotel_chain(request, id):
    hotels_chain_listings = hotel.objects.raw('SELECT * FROM app_hotel where chain_id_id = '+str(id)+' ORDER BY rating DESC')
    return render(request, "index.html",{
        "hotels_listings": hotels_chain_listings
    })

