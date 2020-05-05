from django.shortcuts import render
from django.http import HttpResponse
from .models import Hotel
from .bus_and_hotel import create_bus
place_name = ''     # this is to print the place name which is being searched


def create_hotels():
    hotels = []

    hotel1 = Hotel()
    hotel1.name = 'Capital O'
    hotel1.type = 'AC Ultra Delux'
    hotel1.price = '1500 INR'
    hotel1.location = 'Central sheshadripuram'
    hotels.append(hotel1)

    hotel2 = Hotel()
    hotel2.name = 'Savi Sagar'
    hotel2.type = 'AC Delux'
    hotel2.price = '1300 INR'
    hotel2.location = 'Rajajinagar'
    hotels.append(hotel2)

    hotel3 = Hotel()
    hotel3.name = 'Rajadhani'
    hotel3.type = 'AC Ultra Delux'
    hotel3.price = '2000 INR'
    hotel3.location = 'Basavanagudi'
    hotels.append(hotel3)

    return hotels


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
    hotels = create_hotels()
    buses = create_bus()
    return render(request, 'booking_page.html', {'place' : place_name, 'buses' : buses, 'hotels' : hotels})


def booking_confirm(request, busid):
    return HttpResponse('<h1> all set </h1>')
