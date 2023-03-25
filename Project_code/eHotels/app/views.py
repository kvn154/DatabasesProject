from django.shortcuts import render
from .models import hotels_listings

# Create your views here.
def index(request):
    hotels_listing = hotels_listings.objects.all().order_by('-rating')
    close_listing = list()
    # for lis in hotels_listing:
    #     if bid.objects.filter(product_id=lis.id).order_by('-bid').first():
    #         lis.starting_bid = bid.objects.filter(product_id=lis.id).order_by('-bid').first().bid
    #         if not lis.is_active:
    #             if bid.objects.filter(product_id=lis.id).order_by('-bid').first().user_id == request.user:
    #                 close_listing.append(lis)

    return render(request, "index.html",{
        "hotels_listings": hotels_listing
    })