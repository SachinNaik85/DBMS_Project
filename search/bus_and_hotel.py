import mysql.connector
from essential import credential


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

    class Hotel:
        name = str
        type = str
        price = str
        location = str

    for i in hotel_data:
        hotel1 = Hotel()
        hotel1.name = i[0]
        hotel1.type = i[1]
        hotel1.price = str(i[3]) + ' INR'
        hotel1.location = i[2]
        hotels.append(hotel1)
    print(hotels)

    return hotels




