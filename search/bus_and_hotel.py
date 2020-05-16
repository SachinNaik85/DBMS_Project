import mysql.connector
from essential import credential


def create_bus():
    db = mysql.connector.connect(host="localhost", user="root", passwd=credential['password'], database="travel")
    sql = db.cursor()
    sql.execute("select * from bus;")
    busdata = sql.fetchall()
    buses = []
    sql.close()

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
    db = mysql.connector.connect(host="localhost", user="root", passwd=credential['password'], database="travel")
    sql = db.cursor()
    sql.execute("select * from hotel;")
    hotel_data = sql.fetchall()
    hotels = []
    sql.close()

    class Hotel:
        name = str
        type = str
        price = str
        location = str

    for i in hotel_data:
        hotel1 = Hotel()
        hotel1.name = i[0]
        hotel1.type = i[1]
        hotel1.price = i[2]
        hotel1.location = i[3]
        hotels.append(hotel1)
    print(hotels)

    return hotels




