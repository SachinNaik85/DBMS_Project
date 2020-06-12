import mysql.connector
from essential import credential
from .models import Bus, Hotel, Bus_bookings, Hotel_bookings
from travel import  service


def create_bus(source, destination):
    try:
        db = mysql.connector.connect(host="localhost", user="root", passwd=credential['password'], database="travel")
        sql = db.cursor()
        try:
            query = f'select * from bus where source like "%{source}%" and destination like "%{destination}%"'
            sql.execute(query)
        except mysql.connector.ProgrammingError as e:
            print(e)
        busdata = sql.fetchall()
        buses = []
    except mysql.connector.Error as e:
        print(e)
        pass
    finally:
        sql.close()

    for i in busdata:
        bus1 = Bus()
        bus1.busID = i[0]
        bus1.departure_time = i[1]
        bus1.arrival_time = i[2]
        bus1.busDesc = i[3]
        bus1.price = str(i[4]) + ' INR'
        buses.append(bus1)

    return buses


def create_hotel(destination):
    try:
        db = mysql.connector.connect(host="localhost", user="root", passwd=credential['password'], database="travel")
        sql = db.cursor()
        try:
            query = f'select * from hotel where location like "%{destination}%"'
            sql.execute(query)
        except mysql.connector.ProgrammingError as e:
            print(e)
        hotel_data = sql.fetchall()
        hotels = []
    except mysql.connector.Error as e:
        print(e)
        pass
    finally:
        sql.close()

    for i in hotel_data:
        hotel1 = Hotel()
        hotel1.name = i[0]
        hotel1.type = i[1]
        hotel1.price = str(i[3]) + ' INR'
        hotel1.location = i[2]
        hotels.append(hotel1)
    print(hotels)

    return hotels


def booked_bus():
    username = service.read_name()
    query = f'select * from bus_bookings where username = "{username}"'
    booking_data = service.execute_query(query)
    buses = []
    for i in booking_data:
        obj = Bus_bookings()
        obj.busname = i[0]
        obj.booking_date = i[2]
        obj.booking_time = i[3]
        obj.journey_date = i[4]
        obj.seats = i[5]
        obj.amount = i[6]
        query = f'select departure_time, arrival_time from bus where busid = "{i[0]}"'
        bus_time = service.execute_query(query)
        obj.departure = bus_time[0][0]
        obj.arrival = bus_time[0][1]
        buses.append(obj)
    return buses


def booked_hotels():
    username = service.read_name()
    query = f'select * from hotel_bookings where username = "{username}"'
    data = service.execute_query(query)
    hotels = []
    for i in data:
        obj = Hotel_bookings()
        obj.name = i[0]
        obj.booking_date = i[2]
        obj.booking_time = i[3]
        obj.checkin = i[4]
        obj.checkout = i[5]
        obj.guests = i[6]
        obj.rooms = i[7]
        obj.amount_paid = i[8]
        hotels.append(obj)
    return hotels

