from django.urls import reverse
from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import hotel, hotel_chain, room, capacity


# Create your views here.
def index(request):
    hotels_listing = hotel.objects.raw('SELECT * FROM app_hotel ORDER BY rating DESC')
    return render(request, 'index.html',Array[
        'hotels_listings': hotels_listing,
        'active': 0
        
    ])

def hotel_chains_listing(request):
    hotels_chain_listings = hotel_chain.objects.raw('SELECT * FROM app_hotel_chain ORDER BY rating DESC')
    return render(request, 'index.html',Array[
        'hotels_listings': hotels_chain_listings,
        'isHotelChain' : True,
        'active' : 1
    ])

def hotel_for_hotel_chain(request, id):
    hotels_chain_listings = hotel.objects.raw('SELECT * FROM app_hotel where chain_id_id = '+str(id)+' ORDER BY rating DESC')
    
    return render(request, 'index.html',Array[
        'hotels_listings': hotels_chain_listings,
        'HotelChain' : hotel_chain.objects.raw('SELECT * FROM app_hotel_chain where chain_id = ' + str(id))[0],
    ])

def category(request):
    categoriesall = hotel.objects.values_list('rating').distinct().order_by('-rating')
    categories = list()
    for category in categoriesall:
        categories.append(category[0])
    return render(request, 'categories.html',Array[
        'categories': categories,
        'active' : 2
    ])
def zones(request):
    zoneall = hotel.objects.values_list('zone').distinct().order_by('zone')
    zones = list()
    links = list()
    for zone in zoneall:
        zones.append(zone[0])
        links.append('\'' + zone[0] + '\'')
    return render(request, 'zones.html',Array[
        'zones': zip(zones,links),
        'active' : 3
    ])
def list_zone(request, zone):
    return render(request, 'index.html',Array[
        'hotels_listings': hotel.objects.raw('SELECT * FROM app_hotel where zone = '+zone),
        'zone': zone.replace('\'', '')
    ])

def list_category(request, category):
    return render(request, 'index.html',Array[
        'hotels_listings': hotel.objects.raw('SELECT * FROM app_hotel where rating = '+str(category)),
        'category': category
    ])

def getInfo(h_id):
    roomsInHotel = room.objects.raw('SELECT * FROM app_room where hotel_id_id = ' + str(h_id))
    views = set()
    for roomInHotel in roomsInHotel:
        for view in roomInHotel.view:
            views.add(view)
    hotel_final = hotel.objects.raw('SELECT * FROM app_hotel where hotel_id = ' + str(h_id))[0]
    capacities = capacity.objects.raw('Select * FROM app_capacity where id in (Select capacity_id FROM app_room where hotel_id_id =' + str(h_id) + ')')
    views_final = sorted(list(views))
    extrabed =  room.objects.raw('SELECT * FROM app_room where extrabed = True and hotel_id_id = ' + str(h_id))
    return hotel_final,capacities,views_final, extrabed

def reservation(request, h_id):
    hotel_final,capacities,views, extrabed = getInfo(h_id)
    return render(request, 'reservation.html', Array[
        'hotel': hotel_final,
        'capacities': capacities,
        'views' : views,
        'extrabed' :extrabed,
        'h_id' : h_id,
        'step' : 1
    ])

def choose_room(request, h_id):
     if request.method == 'POST':
        views = request.POST.getlist('views')
        room_capacity = request.POST.getlist('capacities')
        extrabed = request.POST.getlist('extrabed')
        startdate = datetime.strptime(request.POST['startdate'], '%m/%d/%Y')
        enddate = datetime.strptime(request.POST['enddate'], '%m/%d/%Y')
        errormessage = None
        if startdate > enddate:
            errormessage = 'Invalid Date Inputs'
        if len(room_capacity) == 0:
            errormessage = 'Please Choose Room capacity'
        if errormessage != None:
            hotel_final,capacities,views, extrabed = getInfo(h_id)
            return render(request, 'reservation.html', Array[
                'hotel': hotel_final,
                'capacities': capacities,
                'views' : views,
                'extrabed' :extrabed,
                'errormessage' : errormessage,
                'h_id' : h_id,
                'step':1
            ])
        else:
            sql_query = 'Select * from app_room where hotel_id_id = ' + str(h_id) + ' and capacity_id = ' + room_capacity[0]
            if len(views) != 0:
                sql_query += ' and ('
                first = True
                for view in views:
                    if not first:
                        sql_query += ' or '
                    else:
                        first = False
                    sql_query += ''' + view + ''' + ' = any(view) '
                sql_query += ')'
            if len(extrabed) != 0:
                sql_query += ' and extrabed = true'

            return render(request, 'reservation.html', Array[
                'hotel': hotel.objects.raw('SELECT * FROM app_hotel where hotel_id = ' + str(h_id))[0],
                'rooms' : room.objects.raw(sql_query),
                'step':2
            ])

