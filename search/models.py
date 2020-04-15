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

