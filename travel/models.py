from django.db import models


class package:
    name : str
    amount : str
    bus : str
    hotel : str
    price : str
    image : str
    id : int


class booked_package:
    pid : int
    booking_date : str
    booking_time : str
    journey_date : str
    bus : str
    hotel : str
    guests : int
    amount_paid : int
