from django.shortcuts import render
from django.http import HttpResponse
from search.bus_and_hotel import create_bus, create_hotel
place_name = ''     # this is to print the place name which is being searched


def home(request):
    global place_name
    try:
        place_name = request.POST['search_place']       # fetching the place name which was searched
    except Exception as e:
        pass
    return render(request, 'search.html', {'place' : place_name})


def features_home(request,  place_from_features):
    global place_name
    try:
        place_name = place_from_features
    except Exception as e:
        pass
    return render(request, 'search.html', {'place' : place_name})


def booking_request(request):
    global place_name
    hotels = create_hotel()
    buses = create_bus()
    return render(request, 'booking_page.html', {'place' : place_name, 'buses' : buses, 'hotels' : hotels})


def booking_confirm(request, busid):
    return HttpResponse('<h1> all set </h1>')
