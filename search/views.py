from django.shortcuts import render
from django.http import HttpResponse
from .models import Bus, Hotel
place_name = ''     # this is to print the place name which is being searched


def create_bus():
    buses = []

    bus1 = Bus()
    bus1.busID = 'VRL 1740'
    bus1.busDesc = 'AC Sleeper (2+1)'
    bus1.departure_time = '22:00 PM'
    bus1.arrival_time = '06:00 AM'
    bus1.price = '1200 INR'
    buses.append(bus1)

    bus2 = Bus()
    bus2.busID = 'SRS 6682'
    bus2.busDesc = ' NON AC Sleeper (2+1)'
    bus2.departure_time = '21:30 PM'
    bus2.arrival_time = '07:00 AM'
    bus2.price = '1000 INR'
    buses.append(bus2)

    bus3 = Bus()
    bus3.busID = 'SriDurgamba'
    bus3.busDesc = ' NON AC Seater/Sleeper (2+1)'
    bus3.departure_time = '20:30 PM'
    bus3.arrival_time = '06:00 AM'
    bus3.price = '900 INR'
    buses.append(bus3)

    return buses


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
    buses = create_bus()
    hotels = create_hotels()
    return render(request, 'booking_page.html', {'place' : place_name, 'buses' : buses, 'hotels' : hotels})

