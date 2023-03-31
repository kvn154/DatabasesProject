from django.shortcuts import render
from .models import hotel, hotel_chain


# Create your views here.
def index(request):
    hotels_listing = hotel.objects.raw('SELECT * FROM app_hotel ORDER BY rating DESC')
    return render(request, "index.html",{
        "hotels_listings": hotels_listing,
        
    })

def hotel_chains_listing(request):
    hotels_chain_listings = hotel_chain.objects.raw('SELECT * FROM app_hotel_chain ORDER BY rating DESC')
    return render(request, "index.html",{
        "hotels_listings": hotels_chain_listings,
        "isHotelChain" : True
    })

def hotel_for_hotel_chain(request, id):
    hotels_chain_listings = hotel.objects.raw('SELECT * FROM app_hotel where chain_id_id = '+str(id)+' ORDER BY rating DESC')
    
    return render(request, "index.html",{
        "hotels_listings": hotels_chain_listings,
        "HotelChain" : hotel_chain.objects.raw('SELECT * FROM app_hotel_chain where chain_id = ' + str(id))[0]
    })

def category(request):
    categoriesall = hotel.objects.values_list('rating').distinct().order_by('-rating')
    categories = list()
    for category in categoriesall:
        categories.append(category[0])
    return render(request, "categories.html",{
        "categories": categories
    })
def zones(request):
    zoneall = hotel.objects.values_list('zone').distinct().order_by('zone')
    zones = list()
    links = list()
    for zone in zoneall:
        zones.append(zone[0])
        links.append("\'" + zone[0] + "\'")
    return render(request, "zones.html",{
        "zones": zip(zones,links)
    })
def list_zone(request, zone):
    return render(request, "index.html",{
        "hotels_listings": hotel.objects.raw('SELECT * FROM app_hotel where zone = '+zone),
        "zone": zone.replace("\'", "")
    })

def list_category(request, category):
    return render(request, "index.html",{
        "hotels_listings": hotel.objects.raw('SELECT * FROM app_hotel where rating = '+str(category)),
        "category": category
    })


