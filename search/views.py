from django.shortcuts import render
from django.http import HttpResponse
from search.bus_and_hotel import create_bus, create_hotel

place_name = ''  # this is to print the place name which is being searched
bus_name = ''


def home(request):
    global place_name
    try:
        place_name = request.POST['search_place']  # fetching the place name which was searched
    except Exception as e:
        pass
    return render(request, 'search.html', {'place': place_name})


def features_home(request, feature_name):
    global place_name
    try:
        place_name = feature_name
    except Exception as e:
        pass
    return render(request, 'search.html', {'place': place_name})


def booking_request(request):
    global place_name
    hotels = create_hotel()
    buses = create_bus()
    return render(request, 'booking_page.html', {'place': place_name, 'buses': buses, 'hotels': hotels})


def book_bus(request, busname):
    if request.method == 'GET':
        hotels = create_hotel()
        buses = create_bus()
        return render(request, 'booking_page.html', {'place': place_name, 'buses': buses,
                                                     'hotels': hotels, 'booking_request': True, 'busname': busname})

    if request.method == 'POST':
        return HttpResponse(f'booking confirmed for bus {busname}')


def book_hotel(request, hotel_name):
    if request.method == 'GET':
        hotels = create_hotel()
        buses = create_bus()
        return render(request, 'booking_page.html', {'place': place_name, 'buses': buses,
                                                     'hotels': hotels, 'hotel_request': True, 'hotel_name': hotel_name})

    elif request.method == 'POST':
        return HttpResponse(f'booking confirmed for hotel {hotel_name}')
