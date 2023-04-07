from django.urls import reverse
from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def index(request):
    hotels_listing = hotel.objects.raw('SELECT * FROM app_hotel ORDER BY rating DESC, name')
    return render(request, "index.html",{
        "hotels_listings": hotels_listing,
        "active": 0
        
    })
def getEmployee(request):
    return  employee.objects.raw(f"Select * from app_employee where ssa = '{request.user.username}'")

def get_hotels_for_employee(request):
    worksfor = works_for.objects.raw(f"Select * from app_works_for where employee_id = '{request.user.username}'")
    if len(worksfor) != 0:
        list_of_hotels = "("
        not_first = False
        for workfor in worksfor:
            if not_first:
                list_of_hotels += ","
            else:
                not_first = True
            list_of_hotels += str(workfor.hotel_id)
        list_of_hotels += ")"
        hotels_listing = hotel.objects.raw(f'SELECT * FROM app_hotel where hotel_id in {list_of_hotels} ORDER BY rating DESC, name')
    else:
        hotels_listing = None
    return hotels_listing

def index_employee(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    employees = getEmployee(request)
    if len(employees) != 1:
        return HttpResponseRedirect(reverse("login"))
    
    return render(request, "index.html",{
        "hotels_listings": get_hotels_for_employee(request=request),
        "active": 0,
        "is_employee" : True,
        "employee" : getEmployee(request)[0]
        
    })

def login_employee(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None and not user.is_superuser: 
            login(request, user)
            return HttpResponseRedirect(reverse("index_employee"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password.",
                "is_employee" : True
            })
    else:
        return render(request, "login.html",{
            "is_employee":True
        })

def logout_employee(request):
    logout(request)
    return HttpResponseRedirect(reverse("index_employee"))
    
def hotel_chains_listing(request):
    hotels_chain_listings = hotel_chain.objects.raw('SELECT * FROM app_hotel_chain ORDER BY rating DESC, name')
    return render(request, "index.html",{
        "hotels_listings": hotels_chain_listings,
        "isHotelChain" : True,
        "active" : 1
    })

def hotel_for_hotel_chain(request, id):
    hotels_chain_listings = hotel.objects.raw('SELECT * FROM app_hotel where chain_id_id = '+str(id)+' ORDER BY rating DESC')
    
    return render(request, "index.html",{
        "hotels_listings": hotels_chain_listings,
        "HotelChain" : hotel_chain.objects.raw('SELECT * FROM app_hotel_chain where chain_id = ' + str(id))[0],
    })

def category(request):
    categoriesall = hotel.objects.values_list('rating').distinct().order_by('-rating')
    categories = list()
    for category in categoriesall:
        categories.append(category[0])
    return render(request, "categories.html",{
        "categories": categories,
        "active" : 2
    })
def zones(request):
    zoneall = hotel.objects.values_list('zone').distinct().order_by('zone')
    zones = list()
    links = list()
    for zone in zoneall:
        zones.append(zone[0])
        links.append("\'" + zone[0] + "\'")
    return render(request, "zones.html",{
        "zones": zip(zones,links),
        "active" : 3
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

def getInfo(h_id):
    roomsInHotel = room.objects.raw('SELECT * FROM app_room where hotel_id_id = ' + str(h_id))
    views = set()
    
    for roomInHotel in roomsInHotel:
        if roomInHotel.view:
            for view in roomInHotel.view:
                views.add(view)
    hotel_final = hotel.objects.raw('SELECT * FROM app_hotel where hotel_id = ' + str(h_id))[0]
    capacities = capacity.objects.raw('Select * FROM app_capacity where id in (Select capacity_id FROM app_room where hotel_id_id =' + str(h_id) + ')')
    views_final = sorted(list(views))
    extrabed =  room.objects.raw('SELECT * FROM app_room where extrabed = True and hotel_id_id = ' + str(h_id))
    return hotel_final,capacities,views_final, extrabed

def start_reservation(request, h_id):
    hotel_final,capacities,views, extrabed = getInfo(h_id)
    return render(request, "reservation.html", {
        "hotel": hotel_final,
        "capacities": capacities,
        "views" : views,
        "extrabed" :extrabed,
        "h_id" : h_id,
        "step" : 1
    })
def available_rooms(h_id, capacity, views, extrabed, start_date, end_date ,price):
    sql_query = f"Select * from app_room where id not in (Select room_id from app_damage) and hotel_id_id = {h_id} and capacity_id = {capacity} "
    sql_query_reservation = f"Select * from app_reservation where hotel_id = {h_id} and capacity_id = {capacity} "
    if price:
        sql_query += f"and price = {price}"
        sql_query_reservation += f" and price = {price}"
    if views and len(views) != 0:
        sql_query += ' and ('
        sql_query_reservation += ' and ('
        first = True
        for view in views:
            if not first:
                sql_query += " or "
                sql_query_reservation += " or "
            else:
                first = False
            sql_query += f"'{view}' = any(view) "
            sql_query_reservation += f"'{view}' = any(view) "
        sql_query += ")"
        sql_query_reservation += ")"
    if len(extrabed) != 0:
        sql_query += " and extrabed = true"
        sql_query_reservation += " and extrabed = true"
    sql_query += " order by price"
    sql_query_reservation += f" and not (end_time < '{start_date}' or start_time > '{end_date}')"

    reserved_rooms = list()
    for rm in reservation.objects.raw(sql_query_reservation):
        rmTuple = (rm.capacity_id, rm.extrabed, rm.price, tuple(sorted(rm.view)))   
        reserved_rooms.append(rmTuple)

    all_rooms = list()
    rooms_for_complete = list()
    for rm in room.objects.raw(sql_query):
        if rm.view:
            rmTuple = (rm.capacity_id, rm.extrabed, rm.price, tuple(sorted(rm.view)))  
        else:
            rmTuple = (rm.capacity_id, rm.extrabed, rm.price, None)  
        if rmTuple not in reserved_rooms: 
            all_rooms.append(rmTuple)
            rooms_for_complete.append(rm)
        elif rmTuple in reserved_rooms:
            reserved_rooms.remove(rmTuple)
    return all_rooms, rooms_for_complete
                    

    
def choose_room(request, h_id):
    if request.method == "POST":
        views = request.POST.getlist('views')
        room_capacity = request.POST.getlist('capacities')
        extrabed = request.POST.getlist('extrabed')
        startdate = datetime.strptime(request.POST["startdate"], '%m/%d/%Y').date()
        enddate = datetime.strptime(request.POST["enddate"], '%m/%d/%Y').date()
        errormessage = None
        if startdate > enddate:
            errormessage = "Invalid Date Inputs"
        if len(room_capacity) == 0:
            errormessage = "Please Choose Room capacity"
        if errormessage != None:
            hotel_final,capacities,views, extrabed = getInfo(h_id)
            return render(request, "reservation.html", {
                "hotel": hotel_final,
                "capacities": capacities,
                "views" : views,
                "extrabed" :extrabed,
                "errormessage" : errormessage,
                "h_id" : h_id,
                "step":1
            })
        else:
            sql_query = 'Select * from app_room where hotel_id_id = ' + str(h_id) + ' and capacity_id = ' + room_capacity[0]
            if views and len(views) != 0:
                sql_query += ' and ('
                first = True
                for view in views:
                    if not first:
                        sql_query += " or "
                    else:
                        first = False
                    sql_query += "'" + view + "'" + " = any(view) "
                sql_query += ")"
            if len(extrabed) != 0:
                sql_query += " and extrabed = true"
            sql_query += " order by price"
            
            final_rooms = list()
            room_no_dup = set()
            availablerooms, not_important = available_rooms(h_id, room_capacity[0], views, extrabed, startdate, enddate, None)
            for rm in room.objects.raw(sql_query):
                if rm.view:
                    rmTuple = (rm.capacity_id, rm.extrabed, rm.price, tuple(sorted(rm.view)))  
                else:
                    rmTuple = (rm.capacity_id, rm.extrabed, rm.price, None)  
                if rmTuple in availablerooms and rmTuple not in room_no_dup:
                    final_rooms.append(rm)
                    room_no_dup.add(rmTuple)

            return render(request, "reservation.html", {
                "hotel": hotel.objects.raw('SELECT * FROM app_hotel where hotel_id = ' + str(h_id))[0],
                "rooms" : final_rooms,
                "step":2,
                "startdate": request.POST["startdate"],
                "enddate": request.POST["enddate"],
                "h_id":h_id
            })
    else:
        return HttpResponseRedirect(reverse("index"))
        
def complete_reservation(request, h_id):
    if request.method == "POST":
        rooms = request.POST.getlist('room')
        purchased_rooms = list()
        number_of_rooms = list()
        startdate = datetime.strptime(request.POST["startdate"], '%m/%d/%Y').date()
        enddate = datetime.strptime(request.POST["enddate"], '%m/%d/%Y').date()
        for room_id in rooms:
            rm = room.objects.raw(f"Select * from app_room where id = {room_id}")[0]
            if rm.extrabed:
                extrabed = [True]
            else:
                extrabed = []
            not_important, all_similar_rooms = available_rooms(h_id, rm.capacity.id, rm.view, extrabed, startdate, enddate, rm.price)
            purchased_rooms.append(all_similar_rooms[0])
            number_of_rooms.append(len(all_similar_rooms))
        startdate = datetime.strptime(request.POST["startdate"], '%m/%d/%Y').date()
        enddate = datetime.strptime(request.POST["enddate"], '%m/%d/%Y').date()
        return render(request, "reservation.html", {
                    "hotel": hotel.objects.raw('SELECT * FROM app_hotel where hotel_id = ' + str(h_id))[0],
                    "rooms" : zip(purchased_rooms, number_of_rooms),
                    "step":3,
                    "startdate": request.POST["startdate"],
                    "enddate": request.POST["enddate"],
                    "h_id": h_id,
                    "number_Of_days": (enddate - startdate).days

                })
    else:
        return HttpResponseRedirect(reverse("index"))

def save_client_if_not_existed(ssa, first_name, middle_name , last_name, address):
    try:
        client_rs = client(ssa = ssa, first_name=first_name,
                            middle_name = middle_name, last_name = last_name,
                            address = address)
        client_rs.save()
        return client_rs
    except:
        return client.objects.get(ssa=ssa)
    
def save_card_if_not_existed(card_number, expiry_date, cvv, name_on_the_card):
    try:
        card_rs = card(card_number= card_number, expiry_date=expiry_date, cvv=cvv, name_on_the_card=name_on_the_card)
        card_rs.save()
        return card_rs
    except:
        return card.objects.get(card_number = card_number)
    
def save_reservation(request, h_id):
    if request.method == "POST":
        ssa =  request.POST["ssa"]
        client_rs = save_client_if_not_existed(ssa = ssa, first_name= request.POST["first_name"],
                        middle_name = request.POST["middle_name"], last_name = request.POST["last_name"],
                        address = request.POST["address"])
        card_number = request.POST["card_number"]
        card_rs = save_card_if_not_existed(card_number=card_number, expiry_date=request.POST["expiry_date"],
                                 cvv=request.POST["cvv"], name_on_the_card=request.POST["name_on_the_card"])
        rooms = request.POST.getlist('rooms')
        startdate = datetime.strptime(request.POST["startdate"], '%m/%d/%Y')
        enddate = datetime.strptime(request.POST["enddate"], '%m/%d/%Y')
        for rm_id in rooms:
            rm = room.objects.raw(f"Select * from app_room where id = {rm_id}")[0]
            for i in range(int(request.POST[f"num_{rm_id}"])):
                reserve_room = reservation(date_of_reservation = datetime.now(), start_time = startdate,
                                           end_time = enddate, client = client_rs, hotel = hotel.objects.get(hotel_id=h_id),
                                           view = rm.view, capacity = rm.capacity, extrabed = rm.extrabed,
                                           price =  rm.price)
                reserve_room.save()
                payement_room = payement(amount = rm.price, client= client_rs, card_info= card_rs)
                payement_room.save()
                payement_for_room = payement_for(reservation= reserve_room, payement=payement_room)
                payement_for_room.save()
        
        return render(request, "reservation.html", {
                    "hotel": hotel.objects.raw('SELECT * FROM app_hotel where hotel_id = ' + str(h_id))[0],
                    "h_id": h_id
                })
    else:
        return HttpResponseRedirect(reverse("index"))

def reservation_listing(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    employees = employee.objects.raw(f"Select * from app_employee where ssa = '{request.user.username}'")
    if len(employees) != 1:
        return HttpResponseRedirect(reverse("login"))
    hotels = get_hotels_for_employee(request=request)
    
    list_of_hotels = "("
    not_first = False
    for hotel_em in hotels:
        if not_first:
            list_of_hotels += ","
        else:
            not_first = True
        list_of_hotels += str(hotel_em.hotel_id)
    list_of_hotels += ")"
    reservation_listing = reservation.objects.raw(f'SELECT * FROM app_reservation where hotel_id in {list_of_hotels} Order by start_time')

    return render(request, "reservation_employee.html",{
        "reservations" : reservation_listing,
        "is_employee" :True,
        "active" : 1,
        "employee" : getEmployee(request)[0]
        
    })
