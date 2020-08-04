import mysql.connector
import mysql.connector.errorcode
from django.shortcuts import render, redirect, HttpResponse
from essential import credential
from travel import service
from search import bus_and_hotel, service as search_service
from threading import Thread

password_reset_data = {}
ask_to_login = ''
booking_confirmed = False
req_package = 0


def home(request):
    global ask_to_login, req_package, booking_confirmed
    package = service.packages()
    dix = {'authenticate': service.read_status(), 'username': service.read_name(), 'login_message': ask_to_login,
           'packages': package, 'req_package': req_package, 'booking_confirmed': booking_confirmed}
    booking_confirmed = False
    req_package = False
    ask_to_login = ''
    return render(request, 'index.html', dix)


def login(request):
    if request.method == 'GET':
        message = ''
        return render(request, 'login.html', {'message': message, 'reset_wizard': False})

    elif request.method == 'POST':
        try:
            db = mysql.connector.connect(user=credential['db_user'], passwd=credential['password'],
                                         database=credential['using_db'], host='localhost')
            sql = db.cursor()
            username = request.POST['username']
            password = request.POST['password']
            try:
                query = f'SELECT EXISTS (select * from user where username="{username}" and password=MD5("{password}"))'
                sql.execute(query)
            except mysql.connector.ProgrammingError as e:
                print(e)
                pass
            authenticated = sql.fetchall()
            if authenticated[0][0]:
                service.write_status(1, username)
                return render(request, 'index.html',
                              {'authenticate': service.read_status(), 'username': service.read_name()})
            else:
                message = 'Invalid credentials'
                return render(request, 'login.html', {'message': message, 'reset_wizard': False})
        except mysql.connector.Error as e:
            print(e)

        finally:
            sql.close()


def signup(request):
    if request.method == 'GET':
        return render(request, 'signin.html')

    elif request.method == 'POST':
        try:
            db = mysql.connector.connect(user=credential['db_user'], passwd=credential['password'],
                                         database=credential['using_db'], host='localhost')
            sql = db.cursor()
            new_username = request.POST['username']
            query = f'select exists(select * from user where username = "{new_username}")'
            sql.execute(query)
            not_valid_username = sql.fetchall()

            if not not_valid_username[0][0]:
                name = request.POST['name']
                username = request.POST['username']
                email = request.POST['email']
                phone = request.POST['phone']
                password = request.POST['password']
                try:
                    query = f'insert into user values ("{username}", "{name}", "{email}", {phone}, MD5("{password}"));'
                    sql.execute(query)
                    db.commit()
                except mysql.connector.IntegrityError as e:
                    print(e)
                except mysql.connector.ProgrammingError as e:
                    print(e)
                    pass
                return render(request, 'index.html')
            elif not_valid_username[0][0]:
                message = 'Username already taken'
                return render(request, 'signin.html', {'error_message': message})

        except mysql.connector.Error as e:
            print(e)

        finally:
            sql.close()


def logout(request):
    service.write_status(0, '')
    return home(request)


def reset_password(request):
    global password_reset_data
    if request.method == 'GET':
        return render(request, 'login.html', {'reset_wizard': True})

    elif request.method == 'POST':
        username_request = request.POST['username_in_reset']
        try:
            db = mysql.connector.connect(user=credential['db_user'], passwd=credential['password'],
                                         database=credential['using_db'], host='localhost')
            sql = db.cursor()
            try:
                query = f'select exists(select * from user where username = "{username_request}")'
                sql.execute(query)
            except mysql.connector.ProgrammingError as e:
                print(e)
                pass
            is_valid_user = sql.fetchall()
            if is_valid_user[0][0]:
                try:
                    query = f'select name, email from user where username = "{username_request}"'
                    sql.execute(query)
                except mysql.connector.ProgrammingError as e:
                    print(e)
                    pass
                data = sql.fetchone()
                name = data[0]
                email = data[1]
                password_reset_data['username'] = username_request
                password_reset_data['secret_key'] = service.reset_mail(name, email)
                password_reset_data['email'] = email
                email = service.shorten_mail(email)
                return render(request, 'login.html',
                              {'allowed_to_reset': True, 'email': email})
            elif not is_valid_user[0][0]:
                return render(request, 'login.html',
                              {'reset_wizard': True, 'error_message': "invalid username"})
        except mysql.connector.Error as e:
            print(e)

        finally:
            sql.close()


def change_password(request):
    global password_reset_data
    key_from_user = int(request.POST['key_from_user'])
    new_password = request.POST['new_password']

    if key_from_user == password_reset_data['secret_key']:
        try:
            db = mysql.connector.connect(user=credential['db_user'], passwd=credential['password'],
                                         database=credential['using_db'], host='localhost')
            sql = db.cursor()
            try:
                query = f'update user set password = md5("{new_password}") ' \
                        f'where username = "{password_reset_data["username"]}" '
                sql.execute(query)
            except mysql.connector.ProgrammingError as e:
                print(e)
                pass
            db.commit()
            return render(request, 'login.html',
                          {'reset_done': True, 'reset_wizard': False, 'allowed_to_reset_password': True})
        except mysql.connector.Error as e:
            print(e)
        finally:
            sql.close()

    elif key_from_user != password_reset_data['secret_key']:
        return render(request, 'login.html',
                      {'allowed_to_reset': True, 'email': password_reset_data['email'],
                       'error_message': "invalid key"})


def mybookings(request):
    global ask_to_login
    if not service.read_status():
        ask_to_login = 'Please login to view your bookings'
        return redirect(to='/')
    buses = bus_and_hotel.booked_bus()
    hotels = bus_and_hotel.booked_hotels()
    packages = service.booked_packages()
    return render(request, 'mybookings.html', {'bus_bookings': buses, 'hotel_bookings': hotels, 'packages': packages,
                                               'username': service.read_name()})


def book_package(request, package_id):
    global req_package, booking_confirmed
    req_package = package_id
    if request.method == 'GET':
        return redirect(to='HomePage')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        guests = request.POST['guests']
        date = request.POST['journey_date']
        query = f'select exists(select * from user where username = "{username}" and password = md5("{password}"))'
        authenticated = service.execute_query(query)
        try:
            if not authenticated[0][0] or not search_service.checkdate(date):
                req_package = package_id
                return redirect(to='HomePage')
        except IndexError as e:
            pass
        else:
            bus = service.execute_query(f'select bus from package where pid = {package_id}')[0][0]
            print(bus)
            hotel = service.execute_query(f'select hotel from package where pid = {package_id}')[0][0]
            print(hotel)
            package_price = service.execute_query(f'select price from package where pid = {package_id}')[0][0]
            print(package_price)
            query = f'insert into package_booking values( {package_id}, "{username}", "{search_service.date()}",' \
                    f'"{search_service.time()}", "{date}" , "{bus}", "{hotel}", {guests}, ' \
                    f'{int(guests) * int(package_price)})'
            try:
                db = mysql.connector.connect(user=credential['db_user'], passwd=credential['password'],
                                             database=credential['using_db'], host='localhost')
                sql = db.cursor()
                try:
                    sql.execute(query)
                    db.commit()
                    data = service.execute_query(f'select name, email from user where username = "{username}"')
                    t1 = Thread(target=service.confirmation_mail(data[0][0], data[0][1],
                                                                 **{'topic': f'package with package id {package_id}, '
                                                                             f'dated : {date}\nWith this package you are getting {bus} bus and {hotel} hotel '
                                                                             f'for {guests} guests\nTotal amount payable is : {int(guests) * int(package_price)} INR'}))
                    booking_confirmed = True
                    t1.start()
                except mysql.connector.ProgrammingError:
                    print(f'error in executing {query}')
                    return redirect(to='HomePage')

            except mysql.connector.Error as e:
                print(e)
            req_package = 0
            return redirect(to='HomePage')
