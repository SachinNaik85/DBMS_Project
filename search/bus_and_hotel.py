import mysql.connector
from essential import credential
db = mysql.connector.connect(host="localhost", user="root", passwd=credential, database="travel")
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





