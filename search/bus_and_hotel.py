import mysql.connector
from essential import credential
db = mysql.connector.connect(host="localhost", user="root", passwd=credential['password'], database="travel")
sql = db.cursor()


def create_bus():
    sql.execute("select * from bus;")
    busdata = sql.fetchall()
    buses = []

    class Bus:
        busID = str
        busDesc = str
        departure_time = str
        arrival_time = str
        price = str

    for i in busdata:
        bus1 = Bus()
        bus1.busID = i[0]
        bus1.departure_time = i[1]
        bus1.arrival_time = i[2]
        bus1.busDesc = i[3]
        bus1.price = str(i[4]) + ' INR'
        buses.append(bus1)

    return buses


def create_hotel():
    sql.execute("select * from bus;")
    hotel_data = sql.fetchall()
    hotels = []

    class Hotel:
        hotel_name = str
        hotel_type = str
        hotel_price = str
        hotel_location = str

    for i in hotel_data:
        hotel1 = Hotel()
        hotel1.hotel_name = i[0]
        hotel1.hotel_type = i[1]
        hotel1.hotel_price = i[2]
        hotel1.hotel_location = i[3]
        hotels.append(hotel1)

    return hotels




