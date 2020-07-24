from django.shortcuts import render, redirect
# from django.http import HttpResponse
from search.bus_and_hotel import create_bus, create_hotel
import mysql.connector
from essential import credential
from . import service
import travel.service as travel_service
from threading import Thread

redirect_status = False
confirm_status = False
credential_error = False


def home(request):
    try:
        destination = request.POST['destination']  # fetching the place name which was searched
        origin = request.POST['origin']
        service.write_file(origin, destination)
    except Exception as e:
        print(e)
        pass
    place = service.read_file()
    dataset = {'place': place[1]}
    return render(request, 'search.html', dataset)


def features_home(request, feature_name):
    try:
        destination = feature_name
        service.write_file('', destination)
    except Exception as e:
        print(e)
        pass
    place = service.read_file()
    dataset = {'place': place[1]}
    return render(request, 'search.html', dataset)


def booking_request(request):
    global confirm_status
    place = service.read_file()
    hotels = create_hotel(place[1])
    buses = create_bus(place[0], place[1])
    dataset = {'buses': buses, 'hotels': hotels, 'place': place[1]}
    if confirm_status:
        dataset['booking_confirmed'] = True
        confirm_status = False
    print(dataset)
    return render(request, 'booking_page.html', dataset)


def book_bus(request, busname):
    global redirect_status, confirm_status
    place = service.read_file()
    hotels = create_hotel(place[1])
    buses = create_bus(place[0], place[1])
    if request.method == 'GET':
        dataset = {'place': place[1], 'buses': buses, 'hotels': hotels,
                   'booking_request': True, 'busname': busname, }
        if redirect_status:
            redirect_status = False
            dataset['error_message'] = "Invalid credentials"

        return render(request, 'booking_page.html', dataset)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        date = request.POST['date']
        seats = request.POST['seats']

        try:
            db = mysql.connector.connect(host=credential['host'], user=credential['db_user'],
                                         passwd=credential['password'], database=credential['using_db'])
            sql = db.cursor()

            allowed_to_book = service.auth_user(username, password)
            if not allowed_to_book:
                redirect_status = True
                return redirect(to='book_bus', busname=busname, )

            if allowed_to_book:
                fair_date = service.checkdate(date)
                if not fair_date:
                    return redirect('book_bus', busname=busname)

                elif fair_date:
                    try:
                        query = f'insert into bus_bookings values( "{busname}", "{username}", ' \
                                f'"{service.date()}", "{service.time()}" ,"{date}" , {seats} ,' \
                                f'{service.calc_amount(busname, seats)})'

                        print(query)
                        sql.execute(query)
                        db.commit()
                        data = travel_service.execute_query(f'select name, email from user '
                                                            f'where username = "{username}"')
                        t1 = Thread(target=travel_service.confirmation_mail(data[0][0], data[0][1],
                                                                            **{
                                                                                'topic': f'Bus with busid {busname} dated {date}, '
                                                                                         f'for {seats} seats\nTotal amount payable is : '
                                                                                         f'{service.calc_amount(busname, seats)} INR'}))
                        confirm_status = True
                        t1.start()
                        return redirect(to='booking_page')
                    except mysql.connector.ProgrammingError as e:
                        print(e)
                        return redirect('book_bus', busname=busname)

        except mysql.connector.Error as e:
            print(e)
            return redirect('book_bus', busname=busname)


def book_hotel(request, hotel_name):
    global credential_error, confirm_status
    if request.method == 'GET':
        place = service.read_file()
        hotels = create_hotel(place[1])
        buses = create_bus(place[0], place[1])
        dataset = {'place': place[1], 'buses': buses,
                   'hotels': hotels, 'hotel_request': True, 'hotel_name': hotel_name}
        if credential_error:
            dataset['error_message'] = "Invalid credentials"
            credential_error = False
        return render(request, 'booking_page.html', dataset)

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        checkin = request.POST['checkin']
        checkout = request.POST['checkout']
        guests = request.POST['guests']
        rooms = request.POST['rooms']
        print('fetched data success')
        valid_date = service.checkdate(checkin) and service.checkdate(checkout)
        days = service.count_days(checkin, checkout)
        valid_user = service.auth_user(username, password)

        if not valid_user or not valid_date or not days:
            credential_error = True
            return redirect(to='book_hotel', hotel_name=hotel_name)

        elif valid_user and days and valid_date:
            try:
                db = mysql.connector.connect(host="localhost", user="root", passwd=credential['password'],
                                             database="travel")
                sql = db.cursor()
                try:
                    query = f'insert into hotel_bookings values("{hotel_name}", "{username}", "{service.date()}",' \
                            f'"{service.time()}", "{checkin}", "{checkout}", {guests}, {service.calc_rooms(guests, rooms)},' \
                            f'{service.hotel_price(hotel_name, guests, rooms, checkin, checkout)})'
                    sql.execute(query)
                    print(query)
                    db.commit()
                    confirm_status = True
                    data = travel_service.execute_query(f'select name, email from user where username = "{username}"')
                    amount = service.hotel_price(hotel_name, guests, rooms, checkin, checkout)
                    t1 = Thread(target=travel_service.confirmation_mail(data[0][0], data[0][1],
                                                                        **{
                                                                            'topic': f'Hotel with hotelname {hotel_name} \ndated  checkin : {checkin} '
                                                                                     f'checkout : {checkout}, for {guests} guests and {rooms} rooms '
                                                                                     f'\nTotal amount payable is : {amount} INR'}))
                    t1.start()
                    return redirect(to='booking_page')

                except mysql.connector.ProgrammingError as e:
                    print(e)
                    pass

            except mysql.connector.Error as e:
                print(e)
                pass
