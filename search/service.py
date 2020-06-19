import datetime as dt
import mysql.connector
from essential import credential
from math import ceil


def checkdate(date_):
    today = str(dt.datetime.date(dt.datetime.now()))
    date_ = int(str(date_).replace('-', ''))
    today = today.replace('-', '')
    if int(today) > int(date_):
        return False
    else:
        return True


def time():
    return str(dt.datetime.time(dt.datetime.now()))[:8]

print(time())
def calc_amount(busname, seats):
    try:
        db = mysql.connector.connect(host="localhost", user="root", passwd=credential['password'],
                                     database="travel")
        sql = db.cursor()

        try:
            query = f'select price from bus where busid = "{busname}"'
            sql.execute(query)
            price = sql.fetchall()
            return int(price[0][0]) * int(seats)
        except mysql.connector.ProgrammingError as e:
            print(e)
            return -1
    except mysql.connector.Error as e:
        print(e)
        return -1


def date():
    return str(dt.datetime.date(dt.datetime.now()))


def write_file(origin, destination):
    print('writing to file')
    file = open('search.txt', 'w')
    file.writelines(origin)
    file.writelines('\n')
    file.writelines(destination)
    file.close()


def read_file():
    print('reading from file')
    file = open('search.txt', 'r')
    place = file.read().split()
    file.close()
    return place


def auth_user(username, password):
    try:
        db = mysql.connector.connect(host="localhost", user="root", passwd=credential['password'],
                                     database="travel")
        sql = db.cursor()

        try:
            query = f'select exists (select * from user where username="{username}" and password=md5("{password}"))'
            sql.execute(query)
            authenticated = sql.fetchall()
            return bool(authenticated[0][0])
        except mysql.connector.Error as e:
            print(e)
            pass
    except mysql.connector.Error as e:
        print(e)
        pass


def count_days(checkin, checkout):
    checkin = checkin.split('-')
    checkout = checkout.split('-')
    checkin_date = dt.date(int(checkin[0]), int(checkin[1]), int(checkin[2]))
    checkout_date = dt.date(int(checkout[0]), int(checkout[1]), int(checkout[2]))
    return (checkout_date - checkin_date).days


def calc_rooms(guests, rooms):
    if ceil(int(guests)/3) <= int(rooms):
        return int(rooms)
    else:
        return ceil(int(guests)/3)


def hotel_price(hotel_name, guests, rooms, checkin, checkout):
    try:
        db = mysql.connector.connect(host="localhost", user="root", passwd=credential['password'],
                                     database="travel")
        sql = db.cursor()

        try:
            query = f'select price from hotel where hotelname = "{hotel_name}"'
            sql.execute(query)
            price = sql.fetchall()
            return int(price[0][0]) * calc_rooms(guests, rooms) * count_days(checkin, checkout)
        except mysql.connector.ProgrammingError as e:
            print(e)
            pass

    except mysql.connector.Error as e:
        print(e)

