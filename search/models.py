from django.db import models


class Bus:
    busID = str
    busDesc = str
    departure_time = str
    arrival_time = str
    price = str


class Hotel:
    name = str
    type = str
    price = str
    location = str


class Bus_bookings:
    busname : str
    journey_date : str
    amount : str
    seats : str
    booking_time : str
    booking_date : str
    departure : str
    arrival : str


class Hotel_bookings:
    name = str
    date = str
    amount_paid = str
    rooms = str
    guests = str
    booking_date = str
    booking_time = str
    checkin = str
    checkout = str
